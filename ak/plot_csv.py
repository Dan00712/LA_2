#!/bin/env python
import argparse
from pathlib import Path
import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import curve_fit_slits as cfs

ABSOLUTE_ERROR = 80 # mV
fmts=[
        'rs',
        'bo',
        'b^'
]


def main():
    args = parser.parse_args()
    file = Path(args.file)
    assert file.exists() and file.suffix == '.csv'

    df = pd.read_csv(file)
    max_amplitude = df['amp'].max()
    error = ABSOLUTE_ERROR / max_amplitude
    df['amp'] = df['amp'] /max_amplitude    # normalize amplitudes

    handle_ideal_plot(df, args.reg_mode, args.reg_fmt, args.mirror)

    handle_csv_plot(df, args.has_state, args.mirror, lambda _: error)

    plt.xlabel('Rotation entlang des Kreises /°')
    plt.ylabel('normierte Amplitude / $\\left(\\frac{A}{A_0}\\right)$')
    plt.legend()

    if args.outfile is not None:
        outfile = args.outfile
    else:
        outfile = file.parent/(file.stem + '.png')

    plt.savefig(outfile)
     

def handle_csv_plot(df, has_state, mirror, error):
    # plot min and max in different colors, column is state
    # valid values are:
    #   m...Maximum
    #   i...infinum (minium)
    #    ...(empty) neither minimum nor maximum
    # only if --has-state is set
    if has_state and 'state' in df:
        for ((name, sf), fmt) in zip(df.groupby('state'), fmts):
            if name == 'm':
                label = 'gemessene Maxima'
            elif name == 'i':
                label = 'gemessene Minima'
            else:
                label = 'andere Messpunkte'
            plot_df(sf, fmt, mirror, error, label)
    else:
        plot_df(df, fmts[0], mirror, error)


def plot_df(df, fmt, mirror, error, label='gemessene Amplituden'):
    plt.errorbar(df['deg'], df['amp'], 
                 fmt=fmt,
                 xerr=[1 for _ in df['deg']],
                 yerr=[error(A) for A in df['amp']],
                 label=label
                 )
    if mirror:
        plt.errorbar(-df['deg'], df['amp'], 
                     fmt=fmt, 
                     xerr=[1 for _ in df['deg']],
                     yerr=[error(A) for A in df['amp']]
                    )


def handle_ideal_plot(df, reg_mode, reg_fmt, mirror):
    # do nothing if not in list or if none, 
    #   none must be first element
    if reg_mode.lower() == 'none':
        return

    x, y = IDEALISATION_FS[reg_mode](df, mirror)
    if reg_mode == 'single_max':
        label = 'einhüllende Kurve'
    else:
        label = 'idealle Amplitude'
    plt.plot(x, y, reg_fmt,
             label=label
    )
        

def single(df, mirror):
    return ideal_gen(df, mirror, cfs.fit_single_slit)

def single_max(df, mirror):
    assert 'state' in df
    return ideal_gen(df[df['state'] == 'm'], mirror, cfs.fit_single_slit_no)


def double(df, mirror):
    return ideal_gen(df, mirror, cfs.fit_double_slit)

def ideal_gen(df, mirror, fitter):
    popts = fitter(df)
    alpham = df['deg'].max()
    if mirror:
        alpha = np.linspace(-alpham, alpham, 200)
    else:
        alpha = np.linspace(0, alpham, 200)
    return (alpha, cfs.single_slit(alpha, *popts))


IDEALISATION_FS = {'single': single, 'double': double, 'single_max': single_max}
IDEALISATIONS=list(IDEALISATION_FS.keys()) + ['none']

parser = argparse.ArgumentParser()
parser.add_argument('file', type=Path)
parser.add_argument('--reg-mode', choices=IDEALISATIONS, default='none')
parser.add_argument('--reg-fmt', default='--m')
parser.add_argument('--has-state', action=argparse.BooleanOptionalAction, default=True)
parser.add_argument('-o', '--outfile', type=Path, default=None)
parser.add_argument('--mirror', action=argparse.BooleanOptionalAction, default=False)

if __name__ == '__main__':
    main()

