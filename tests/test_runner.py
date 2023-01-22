from src.kanban_metrics.runner import Runner
from tests.configurable_argument_parser import ConfigurableArgumentParser
from tests.histogram_stub import HistogramStub


def test_main_calls_plot_with_parsed_data():
    histogram = HistogramStub()

    Runner(ConfigurableArgumentParser("data/sample.csv"), histogram).run()

    assert histogram.min_lead_time == 2
    assert histogram.max_lead_time == 5
