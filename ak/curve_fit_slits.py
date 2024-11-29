import numpy as np
import scipy.optimize as opt

LAMBDA = 0.8 /100 # m
K = 2*np.pi /LAMBDA

def single_slit(alpha, b, offset):
    alpha = alpha * 2*np.pi /360    # transform to rad
    return (np.sinc(K/2 * b * np.sin(alpha)))**2 + offset

def double_slit(alpha, a, b, offset):
    alpha = alpha * 2*np.pi /360    # transform to rad
    return (np.sinc(K/2 * b * np.sin(alpha)))**2 \
            * (np.cos(K/2 * a * np.sin(alpha)))**2 + offset

def fit_single_slit(df):
    alpha = df['deg']
    amp = df['amp']

    res =  opt.curve_fit(single_slit,
                  alpha,
                  amp,
                  [LAMBDA/50, 0]
    )[0]
    df['amp'] = df['amp'] - res[-1]
    res = list(res[:-1]) + [0]

    return res


def fit_double_slit(df):
    alpha = df['deg']
    amp = df['amp']

    res = opt.curve_fit(double_slit,
                  alpha,
                  amp,
                  [LAMBDA, 1, 0]
    )[0]
    return res

