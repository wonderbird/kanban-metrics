from src.kanban_metrics.histogram import Histogram


class HistogramStub(Histogram):
    """Collect data given to the plot function for testing."""

    def __init__(self):
        self.min_lead_time = None
        self.max_lead_time = None

    def plot(self, bins, frequencies_per_bin):
        index_of_min_lead_time = next(
            index for index, value in enumerate(frequencies_per_bin) if value > 0
        )
        self.min_lead_time = bins[index_of_min_lead_time]

        index_of_max_lead_time = next(
            index
            for index, value in reversed(list(enumerate(frequencies_per_bin)))
            if value > 0
        )
        self.max_lead_time = bins[index_of_max_lead_time]
