#!/usr/bin/env python3

from src.kanban_metrics.command_line_argument_parser import CommandLineArgumentParser
from src.kanban_metrics.histogram_plotter import HistogramPlotter
from src.kanban_metrics.runner import Runner


if __name__ == "__main__":
    Runner(CommandLineArgumentParser(), HistogramPlotter()).run()
