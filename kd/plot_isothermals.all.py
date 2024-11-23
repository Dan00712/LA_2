from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


CROSS_SECTION = 3.14        # (cm)^2
perr = 60/100               # preassure error is 1% of 60 bar


def main():
    p = Path(".") /"datas"  # folder where data is stored
    fmts = [
        'o',
        's',
        'x',
        'D'
    ]

    # all files in data must start with isotherm for them to be converted to plots
    for d, fmt in zip(
            filter(lambda path: path.suffix == '.csv' and path.name.startswith("isotherm") ,p.iterdir()),
            fmts):
        # the data is saved in csv format and assumed to have the columns
        # T/°C, s/mm, p/bar, Phase
        df = pd.read_csv(d)


        ps = df.iloc[:, 2]  # overpreassure is already compensated
        ss = df.iloc[:, 1]/10   # in cm
        Vs = ss * CROSS_SECTION # in cm^3

        T  = df.iloc[0,0]   # Temperature is constant

        plt.ylabel("p /bar")
        plt.xlabel("V /cm$^3$")
        plt.errorbar(
                Vs, ps,
                label=f"gemessene Isotherme bei {T:>.1f}°C",
                yerr=[perr for _ in ps],
                fmt=fmt
                )

    plt.legend()
    plt.savefig("isothermals.all" + ".png", dpi=300)


if __name__ == '__main__':
    main()
