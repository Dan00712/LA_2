import numpy as np
import scipy.optimize as opt

LAMBDA = 0.8 / 100  # m
K = 2 * np.pi / LAMBDA


def single_slit(alpha, b, A, offset):
    alpha = alpha * 2 * np.pi / 360  # transform to rad
    return A * abs(np.sinc(K / 2 * b * np.sin(alpha))) + offset


def single_slit_no(alpha, b, A):
    return single_slit(alpha, b, A, 0)


def double_slit(alpha, a, b, A):
    alpha = alpha * 2 * np.pi / 360  # transform to rad
    return (
        A
        * abs(np.sinc(K / 2 * b * np.sin(alpha)))
        * abs(np.cos(K / 2 * a * np.sin(alpha)))
    )


def fit_single_slit(df):
    alpha = df["deg"]
    amp = df["amp"]

    res = opt.curve_fit(single_slit, alpha, amp, [LAMBDA / 50, 1, 0])[0]

    return res


def fit_single_slit_no(df):
    alpha = df["deg"]
    amp = df["amp"]

    res = opt.curve_fit(single_slit_no, alpha, amp, [LAMBDA / 50, 1])[0]

    return list(res) + [0]


def fit_double_slit(df):
    alpha = df["deg"]
    amp = df["amp"]

    res = opt.curve_fit(double_slit, alpha, amp, [LAMBDA, 1, 1])[0]
    return res
