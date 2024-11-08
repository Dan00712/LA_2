from sys import exit
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as opt


CROSS_SECTION = 3.13 / 100  # m^2
perr = 60 / 100


def main():
    p = Path(".") / "datas"

    for d in filter(
        lambda path: path.suffix == ".csv" and path.name.startswith("isotherm"),
        p.iterdir(),
    ):
        df = pd.read_csv(d)
        name = d.stem
        print(name)

        fig, ax = plt.subplots()

        ps = df.iloc[:, 2]
        ss = df.iloc[:, 1]
        T = df.iloc[0, 0]

        ax.set_xlabel("s /mm")
        ax.set_ylabel("p /bar")

        ax.errorbar(
            ss,
            ps,
            label=f"gemessene Isotherme bei {T}°C",
            color="r",
            yerr=[perr for _ in ps],
            fmt="o",
        )

        fig.savefig(name + ".png", dpi=300)


if __name__ == "__main__":
    main()
