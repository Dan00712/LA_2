import argparse
from pathlib import Path
import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# a script to plot the interference patterns in the experiments
#   2.1; 2.2; 2.3; 2.4
# cli args: csv files


LAMBDA = 0.8 /100 # m
K = 2*np.pi/LAMBDA
IDEALISATIONS=[
    'none',
    'single',
    'double'
]

parser = argparse.ArgumentParser()
parser.add_argument('file', type=Path)
parser.add_argument('--reg-mode', choices=IDEALISATIONS, default='none')
parser.add_argument('--reg-fmt', default='--c')
parser.add_argument('--has-state', action=argparse.BooleanOptionalAction, default=True)
parser.add_argument('--outfile', type=Path, default=None)
parser.add_argument('--d-screen', type=float, default=0.0)
parser.add_argument('--d-slits', type=float, default=0.0)
parser.add_argument('--mirror', action=argparse.BooleanOptionalAction, default=False)
fmts=[
        'rs',
        'bo',
        'g^'
]


def main():
    args = parser.parse_args()
    file = Path(args.file)
    assert file.exists() and file.suffix == '.csv'

    df = pd.read_csv(file)
    max_amplitude = df['amp'].max()
    df['amp'] = df['amp'] /max_amplitude    # normalize amplitudes

    handle_csv_plot(df, args.has_state, args.mirror)
    #handle_ideal_plot(args.reg_mode, args.reg_fmt)

    if args.outfile and args.outfile.is_file():
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
            plot_df(sf, fmt, mirror)
    else:
        plot_df(df, fmts[0], mirror)


def plot_df(df, fmt, mirror):
    plt.plot(df['deg'], df['amp'], fmt,
             label='gemessene Amplituden')
    if mirror:
        plt.plot(-df['deg'], df['amp'], fmt)

def handle_ideal_plot(reg_mode, reg_fmt, d, L, a):
    # do nothing if not in list or if none, 
    #   none must be first element
    if reg_mode.to_lower() not in IDEALISATIONS[1:]:
        return

    funcs = {'single': single, 'double': double}
    x, y = funcs[args.reg_mode](args)
    plt.plot(x, y, reg_fmt,
             label='idealle Amplitude'
    )
        

def single(d, L, a, k):
    pass

def double(d, L, a, k):
    pass


if __name__ == '__main__':
    main()

