from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


CROSS_SECTION = 3.14 # cm^2
perr = 60 / 100  # preassure error is 1% of 60 bar
Terr = 1.5  # temperature error is ~ +-1.5°C

def main():
    p = Path(".") /"datas"
    fmts = [
        'o',
        's',
        'x',
        'D'
    ]

    # all files in data must start with isochor for them to be converted to plots
    for d, fmt in zip(
            filter(lambda path: path.suffix == '.csv' and path.name.startswith("isochor"), p.iterdir()),
            fmts
            ):

        # the data is saved in csv format and assumed to have the columns
        # T/°C, s/mm, p/bar, Phase
        df = pd.read_csv(d)

        ps = df.iloc[:, 2]  # overpreassure is already compensated
        Ts = df.iloc[:, 0]

        s  = df.iloc[0,1]/10    # s is constant, s in cm
        V = s * CROSS_SECTION   # in cm^2

        plt.xlabel("T /°C")
        plt.ylabel("p /bar")
        plt.errorbar(
                Ts, ps,
                label=f"gemessene Isotherme bei ${V:> 6.2f}cm^3$",
                xerr=[Terr for _ in Ts],
                yerr=[perr for _ in ps],
                fmt=fmt
                )

    plt.legend()
    plt.savefig("isochors.all" + ".png", dpi=300)


if __name__ == "__main__":
    main()
