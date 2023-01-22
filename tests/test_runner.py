from src.kanban_metrics.runner import Runner
from tests.configurable_argument_parser import ConfigurableArgumentParser
from tests.histogram_stub import HistogramStub


def test_main_calls_plot_with_parsed_data():
    args = ConfigurableArgumentParser().parse_custom_args(["data/sample.csv"])
    histogram = HistogramStub()

    Runner(histogram).run(args)

    assert histogram.last_bin == 9
