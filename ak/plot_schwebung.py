import numpy as np
import matplotlib.pyplot as plt


f1 = 40 * 10**3
f2 = f1 + 1.5*10**3


def f(t):
    return np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)


t = np.linspace(0, 2*10**(-3), 5000)
a = f(t)
a = a / a.max()

plt.plot(t*1000, a)
plt.xlabel('t /ms')
plt.ylabel('Normierte Amplitude')

plt.savefig("imgs/beat.png")
