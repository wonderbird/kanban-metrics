#!/usr/bin/env python3

import src.kanban_metrics.argument_parser as argument_parser

from src.kanban_metrics.histogram_plotter import HistogramPlotter
from src.kanban_metrics.runner import Runner


if __name__ == '__main__':
    args = argument_parser.ArgumentParser().parse()
    Runner(HistogramPlotter()).run(args)
