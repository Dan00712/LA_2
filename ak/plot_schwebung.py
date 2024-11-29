import numpy as np
import matplotlib.pyplot as plt


f1 = 40
f2 = f1 + 1.5


def f(t):
    return np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)


t = np.linspace(0, 1.25, 2000)
a = f(t)
a = a / a.max()

plt.plot(t, a)

plt.savefig("imgs/beat.png")
