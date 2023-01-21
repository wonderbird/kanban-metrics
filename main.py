#!/usr/bin/env python3

import argparse

from histogram_plotter import HistogramPlotter
from runner import Runner


def create_argument_parser():
    desc = """Plot kanban diagrams."""
    result = argparse.ArgumentParser(description=desc)
    result.add_argument("filename", help="path to the csv data file")
    return result


if __name__ == '__main__':
    parser = create_argument_parser()
    args = parser.parse_args()
    Runner(HistogramPlotter()).run(args)
