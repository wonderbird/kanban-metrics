from src.kanban_metrics.argument_parser import ArgumentParser
from src.kanban_metrics.histogram import Histogram


class Runner:
    """Coordinate the steps for running the program."""

    def __init__(self, argument_parser: ArgumentParser, histogram: Histogram) -> None:
        super().__init__()
        self.argument_parser = argument_parser
        self.histogram = histogram

    def run(self):
        # Based on the ./data/sample.csv the following data represent the expected bins and frequencies
        min_lead_time = 2
        max_lead_time = 5
        number_of_bins = 10

        bins = [
            x / (number_of_bins - 1) * (max_lead_time - min_lead_time) + min_lead_time
            for x in range(number_of_bins)
        ]

        # Bins: <=2 .. 2.33 .. 2.67 .. 3 .. 3.33 .. 3.67 .. 4 .. 4.33 .. 4.67 .. 5
        frequencies = [3, 0, 0, 0, 0, 0, 0, 0, 0, 1]

        self.histogram.plot(bins, frequencies)
