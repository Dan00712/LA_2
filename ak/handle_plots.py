import numpy as np
import matplotlib.pyplot as plt

import curve_fits as cfs


FMTS = ["rs", "bo", "b^"]


def handle_csv_plot(df, has_state, mirror, error):
    # plot min and max in different colors, column is state
    # valid values are:
    #   m...Maximum
    #   i...infinum (minium)
    #    ...(empty) neither minimum nor maximum
    # only if --has-state is set
    if has_state and "state" in df:
        for (name, sf), fmt in zip(df.groupby("state"), FMTS):
            if name == "m":
                label = "gemessene Maxima"
            elif name == "i":
                label = "gemessene Minima"
            else:
                label = "andere Messpunkte"
            plot_df(sf, fmt, mirror, error, label)
    else:
        plot_df(df, FMTS[0], mirror, error)


def plot_df(df, fmt, mirror, error, label="gemessene Amplituden"):
    plt.errorbar(
        df["deg"],
        df["amp"],
        fmt=fmt,
        xerr=[1 for _ in df["deg"]],
        yerr=[error(A) for A in df["amp"]],
        label=label,
    )
    if mirror:
        plt.errorbar(
            -df["deg"],
            df["amp"],
            fmt=fmt,
            xerr=[1 for _ in df["deg"]],
            yerr=[error(A) for A in df["amp"]],
        )


def handle_ideal_plot(df, reg_mode, reg_fmt, mirror):
    # do nothing if not in list or if none,
    #   none must be first element
    if reg_mode.lower() == "none":
        return

    x, y = IDEALISATION_FS[reg_mode](df, mirror)
    if reg_mode == "single_max":
        label = "einhüllende Kurve"
    else:
        label = "idealle Amplitude"
    plt.plot(x, y, reg_fmt, label=label)


def single(df, mirror):
    return ideal_gen(df, mirror, cfs.fit_single_slit)


def single_max(df, mirror):
    assert "state" in df
    return ideal_gen(df[df["state"] == "m"], mirror, cfs.fit_single_slit_no)


def double(df, mirror):
    return ideal_gen(df, mirror, cfs.fit_double_slit)


def ideal_gen(df, mirror, fitter):
    popts = fitter(df)
    alpham = df["deg"].max()
    if mirror:
        alpha = np.linspace(-alpham, alpham, 200)
    else:
        alpha = np.linspace(0, alpham, 200)
    return (alpha, cfs.single_slit(alpha, *popts))


IDEALISATION_FS = {"single": single, "double": double, "single_max": single_max}
