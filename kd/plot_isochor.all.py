from sys import exit
from pathlib import Path


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as opt


a = 4.265   # N m^4 mol^2
b = 65.8e+6 # m^3 /mol
R = 8.3145  # J /mol /K
CROSS_SECTION = 3.13/100 # m^2

perr = 60/100
Terr = 1.5
def main():
    p = Path(".") /"datas"
    #fig, plt = plt.subplots()
    #cm = mpl.colormaps["plasma"]

    for d in filter(lambda path: path.suffix == '.csv' and path.name.startswith("isochor"), p.iterdir()):
        df = pd.read_csv(d)
        name = d.stem
        print(name)


        ps = df.iloc[:, 2]
        Ts = df.iloc[:, 0]
        s  = df.iloc[0,1]

        plt.xlabel("T /°C")
        plt.ylabel("p /bar")

        print("plottet ", name)
        plt.errorbar(Ts, ps,
                label=f"gemessene Isotherme bei {s}mm",
                xerr=[Terr for _ in Ts],
                yerr=[perr for _ in ps],
                fmt="o"
                )

    plt.set_cmap('jet')
    plt.legend()
    plt.savefig("isochors.all" + '.png', dpi=300)


if __name__ == '__main__':
    main()
