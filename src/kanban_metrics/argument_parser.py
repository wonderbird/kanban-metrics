import argparse


class ArgumentParser:
    """Abstract base class to parse command line arguments."""

    def __init__(self) -> None:
        """Set up the command line arguments and usage help."""

        desc = """Plot kanban diagrams."""
        self.parser = argparse.ArgumentParser(description=desc)
        self.parser.add_argument("filename", help="path to the csv data file")

    def parse(self):
        """Parse the command line arguments and returned the parse result.

        Override this function in an implementation of this abstract base class.
        """
        pass
