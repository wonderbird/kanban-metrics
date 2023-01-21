# Kanban Metrics

Python scripts to generate Kanban metrics and visualizations from CSV input.

## Thanks

Many thanks to [JetBrains](https://www.jetbrains.com/?from=train-delays) who provide
an [Open Source License](https://www.jetbrains.com/community/opensource/) for this project ❤️.

## Prerequisites

```shell
pip install -r requirements.txt
```

## Run

You can run the application from the command line. Then it will open the charts in separate application windows.

```shell
# Print usage information
./main.py --help

# Plot diagrams for the data in ./data/sample.csv
./main.py ./data/sample.csv
```

[./data/sample.csv](./data/sample.csv) is the path to the metrics - the linked file contains some sample data.

As an alternative, run the application from inside [JetBrains PyCharm](https://www.jetbrains.com/pycharm/). You can
configure the data file to be used in the run parameters. In the [Scientific
Mode](https://www.jetbrains.com/help/pycharm/matplotlib-tutorial.html#run), the plots will be shown in the SciView /
Plots area.

## Test

Unit tests are written with [pytest](https://docs.pytest.org/). To run all the tests, enter

```shell
pytest
```
