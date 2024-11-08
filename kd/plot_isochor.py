from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


Perr = 60 / 100
Terr = 1.5


def main():
    p = Path(".") / "datas"

    for d in filter(
        lambda path: path.suffix == ".csv" and path.name.startswith("isochor"),
        p.iterdir(),
    ):
        df = pd.read_csv(d)
        name = d.stem
        print(name)

        fig, ax = plt.subplots()

        ps = df.iloc[:, 2]
        Ts = df.iloc[:, 0]
        s = df.iloc[0, 1]

        plt.xlabel("T /°C")
        plt.ylabel("p /bar")

        plt.errorbar(
            Ts,
            ps,
            label=f"gemessene Isochore bei {s}mm",
            color="r",
            xerr=[Terr for _ in Ts],
            yerr=[Perr for _ in ps],
            fmt="o",
        )
        plt.savefig(d.name + ".png")


if __name__ == "__main__":
    main()
