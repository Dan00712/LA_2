#!/bin/env python
import argparse
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

from handle_plots import IDEALISATION_FS, handle_ideal_plot, handle_csv_plot

ABSOLUTE_ERROR = 80  # mV
IDEALISATIONS = list(IDEALISATION_FS.keys()) + ["none"]

parser = argparse.ArgumentParser()
parser.add_argument("file", type=Path)
parser.add_argument("--reg-mode", choices=IDEALISATIONS, default="none")
parser.add_argument("--reg-fmt", default="--m")
parser.add_argument("--has-state", action=argparse.BooleanOptionalAction, default=True)
parser.add_argument("-o", "--outfile", type=Path, default=None)
parser.add_argument("--mirror", action=argparse.BooleanOptionalAction, default=False)


def main():
    args = parser.parse_args()
    file = Path(args.file)
    assert file.exists() and file.suffix == ".csv"

    df = pd.read_csv(file)
    max_amplitude = df["amp"].max()
    error = ABSOLUTE_ERROR / max_amplitude
    df["amp"] = df["amp"] / max_amplitude  # normalize amplitudes

    handle_ideal_plot(df, args.reg_mode, args.reg_fmt, args.mirror)

    handle_csv_plot(df, args.has_state, args.mirror, lambda _: error)

    plt.xlabel("Rotation entlang des Kreises /$^\\circ$")
    plt.ylabel("normierte Amplitude / $\\left(\\frac{A}{A_0}\\right)$")
    plt.legend()

    if args.outfile is not None:
        outfile = args.outfile
    else:
        outfile = file.parent / (file.stem + ".png")

    plt.savefig(outfile)


if __name__ == "__main__":
    main()
