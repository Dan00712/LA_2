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

def main():
    p = Path(".") /"datas"
    #fig, plt = plt.subplots()
    #cm = mpl.colormaps["plasma"]

    for d in filter(lambda path: path.suffix == '.csv' ,p.iterdir()):
        df = pd.read_csv(d, encoding='cp1252')
        name = d.stem
        print(name)


        ps = df.iloc[:, 2] + 1
        ss = df.iloc[:, 1]
        T  = df.iloc[0,0]

        plt.xlabel("s /mm")
        plt.ylabel("p /bar")

        plt.scatter(ss, ps,
                label=f"gemessene Isotherme bei {T}°C",
    #            color=c
                s = 10
                )

    plt.set_cmap('jet')
    plt.legend()
    plt.savefig("isothermals.all" + '.png', dpi=300)



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
