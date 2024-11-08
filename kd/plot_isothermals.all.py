from sys import exit
from pathlib import Path

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as opt


perr = 60 / 100  # preassure error is 1% of 60 bar


def main():
    p = Path(".") / "datas"  # folder where data is stored

    # all files in data must start with isotherm for them to be converted to plots
    for d in filter(
        lambda path: path.suffix == ".csv" and path.name.startswith("isotherm"),
        p.iterdir(),
    ):

        # the data is saved in csv format and assumed to have the columns
        # T/°C, s/mm, p/bar, Phase
        df = pd.read_csv(d)
        name = d.stem
        print(name)

        p = df.iloc[:, 2]  # overpreassure is already compensated
        s = df.iloc[:, 1]
        T = df.iloc[0, 0]  # Temperature is constant

        plt.xlabel("s /mm")
        plt.ylabel("p /bar")
        plt.errorbar(
            s,
            p,
            label=f"gemessene Isotherme bei {T}°C",
            yerr=[perr for _ in ps],  # error is constant across the range
            fmt="o",
        )

    plt.legend()
    plt.savefig("isothermals.all" + ".png", dpi=300)


if __name__ == "__main__":
    main()
