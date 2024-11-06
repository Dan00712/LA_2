from sys import exit
from pathlib import Path


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as opt


a = 4.265   # N m^4 mol^2
b = 65.8e+6 # m^3 /mol
R = 8.3145  # J /mol /K
CROSS_SECTION = 3.13/100 # m^2

def main():
    p = Path(".") /"datas"

    for d in filter(lambda path: path.suffix == '.csv' ,p.iterdir()):
        df = pd.read_csv(d, encoding='cp1252')
        name = d.stem
        print(name)

        fig, ax = plt.subplots()

        ps = df.iloc[:, 2] + 1
        ss = df.iloc[:, 1]
        T  = df.iloc[0,0]

        ax.set_xlabel("s /mm")
        ax.set_ylabel("p /bar")

        ax.scatter(ss, ps,
                label=f"gemessene Isotherme bei {T}°C",
                color="r"
                )

        fig.savefig(name + '.png', dpi=300)



def pressure(V, T):
    V = V/n
    return R*T/(V - b) - a/V**2

@lambda f: f()
def n():
    P = 22.5e5
    T = 22 + 273.15
    V = 12.03/1000 * CROSS_SECTION

    def vdw(n):
        return (P + (a * n**2) /V**2) * (V - n*b) - n*R*T
    initial_guess = 1
    n_solution, = opt.fsolve(vdw, initial_guess)
    return n_solution

if __name__ == '__main__':
    main()
