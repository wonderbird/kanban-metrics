from src.kanban_metrics.argument_parser import ArgumentParser
from src.kanban_metrics.histogram import Histogram


class Runner:
    """Coordinate the steps for running the program."""
    def __init__(self, argument_parser: ArgumentParser, histogram: Histogram) -> None:
        super().__init__()
        self.argument_parser = argument_parser
        self.histogram = histogram

    def run(self):
        bins = range(10)
        self.histogram.plot(bins, bins)
