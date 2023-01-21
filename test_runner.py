import main
from histogram_stub import HistogramStub
from runner import Runner


def test_main_calls_plot_with_parsed_data():
    parser = main.create_argument_parser()
    cli_arguments = ["data/sample.csv"]
    parsed_arguments = parser.parse_args(cli_arguments)

    histogram = HistogramStub()
    Runner(histogram).run(parsed_arguments)

    assert histogram.last_bin == 9
