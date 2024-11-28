import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# a script to plot the interference patterns in the experiments
#   2.1; 2.2; 2.3; 2.4
# cli args: csv files

parser = argparse.ArgumentParser()
parser.add_argument('file', type=Path)
parser.add_argument('--format', type=list[str], default=['bo', 'rs', 'g^'])
IDEALISATIONS=[
    'none',
    'single',
    'double'
])
parser.add_argument('--reg-mode', choices=IDEALISATIONS)
parser.add_argument('--reg-fmt', default='<y')

def main():
    args = parser.parse_args()
    file = Path(args.file)
    assert file.exists() and file.suffix == '.csv'
    fmt = args.format

    df = pd.read_csv(file)
    # plot min and max in different colors, column is state
    # valid values are:
    #   m...Maximum
    #   i...infinum (minium)
    #    ...(empty) neither minimum nor maximum


def handle_ideal_plot(args):
    # do nothing if not in list or if none, 
    #   none must be first element
    if args.reg_mode.to_lower() not in IDEALISATIONS[1:]:
        return

    funcs = {'single': single, 'double':}
    x, y = funcs[args.reg_mode](args)
    plt.plot(x, y, fmt=args.reg_fmt)
        

def single(args):
    pass

def double(args):
    pass


if __name__ == '__main__':
    main()

