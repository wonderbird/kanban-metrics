class Runner:
    """Coordinate the steps for running the program."""
    def __init__(self, histogram) -> None:
        super().__init__()
        self.histogram = histogram

    def run(self, args):
        bins = range(10)
        self.histogram.plot(bins, bins)
