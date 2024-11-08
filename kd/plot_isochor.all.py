from sys import exit
from pathlib import Path

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as opt


perr = 60 / 100  # preassure error is 1% of 60 bar
Terr = 1.5  # temperature error is ~ +-1.5°C


def main():
    p = path(".") / "datas"  # folder where data is stored

    # all files in data must start with isochor for them to be converted to plots
    for d in filter(
        lambda path: path.suffix == ".csv" and path.name.startswith("isochor"),
        p.iterdir(),
    ):
        # the data is saved in csv format and assumed to have the columns
        # T/°C, s/mm, p/bar, Phase
        df = pd.read_csv(d)

        p = df.iloc[:, 2]  # overpreassure is already compensated
        T = df.iloc[:, 0]
        s = df.iloc[0, 1]  # s is constant

        plt.xlabel("T /°C")
        plt.ylabel("p /bar")

        plt.errorbar(
            T,
            p,
            label=f"gemessene Isotherme bei {s}mm",
            xerr=[Terr for _ in Ts],  # errors are constant across the range
            yerr=[perr for _ in ps],
            fmt="o",
        )

    plt.legend()
    plt.savefig("isochors.all" + ".png", dpi=300)


if __name__ == "__main__":
    main()
