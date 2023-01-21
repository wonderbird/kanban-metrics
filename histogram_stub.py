from histogram import Histogram


class HistogramStub(Histogram):
    """Collect data given to the plot function for testing."""
    def __init__(self):
        self.last_bin = None

    def plot(self, bins, frequencies_per_bin):
        self.last_bin = bins[-1]
