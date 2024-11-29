import argparse
from pathlib import Path
import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import curve_fit_slits as cfs
# a script to plot the interference patterns in the experiments
#   2.1; 2.2; 2.3; 2.4
# cli args: csv files


IDEALISATIONS=[
    'none',
    'single',
    'double'
]

parser = argparse.ArgumentParser()
parser.add_argument('file', type=Path)
parser.add_argument('--reg-mode', choices=IDEALISATIONS, default='none')
parser.add_argument('--reg-fmt', default='--m')
parser.add_argument('--has-state', action=argparse.BooleanOptionalAction, default=True)
parser.add_argument('-o', '--outfile', type=Path, default=None)
parser.add_argument('--mirror', action=argparse.BooleanOptionalAction, default=False)
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
    df['amp'] = df['amp'] /max_amplitude    # normalize amplitudes

    handle_ideal_plot(df, args.reg_mode, args.reg_fmt, args.mirror)

    handle_csv_plot(df, args.has_state, args.mirror)

    plt.xlabel('Rotation entlang des Kreises /°')
    plt.ylabel('normierte Amplitude / $\\left(\\frac{A}{A_0}\\right)$')
    plt.legend()

    if args.outfile is not None:
        outfile = args.outfile
    else:
        outfile = file.parent/(file.stem + '.png')

    plt.savefig(outfile)
     

def handle_csv_plot(df, has_state, mirror):
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
            plot_df(sf, fmt, mirror, label)
    else:
        plot_df(df, fmts[0], mirror)


def plot_df(df, fmt, mirror, label='gemessene Amplituden'):
    plt.plot(df['deg'], df['amp'], fmt,
             label=label)
    if mirror:
        plt.plot(-df['deg'], df['amp'], fmt)


def handle_ideal_plot(df, reg_mode, reg_fmt, mirror):
    # do nothing if not in list or if none, 
    #   none must be first element
    if reg_mode.lower() not in IDEALISATIONS[1:]:
        return

    funcs = {'single': single, 'double': double}
    x, y = funcs[reg_mode](df, mirror)
    plt.plot(x, y, reg_fmt,
             label='idealle Amplitude'
    )
        

def single(df, mirror):
    popts = cfs.fit_single_slit(df)
    alpham = df['deg'].max()
    if mirror:
        alpha = np.linspace(-alpham, alpham, 200)
    else:
        alpha = np.linspace(0, alpham, 200)
    return (alpha, cfs.single_slit(alpha, *popts))


def double(df, mirror):
    popts = cfs.fit_double_slit(df)
    if mirror:
        alpha = np.linspace(-45, 45, 200)
    else:
        alpha = np.linspace(-45, 45, 200)
    return (alpha, cfs.double_slit(alpha, *popts))


if __name__ == '__main__':
    main()

