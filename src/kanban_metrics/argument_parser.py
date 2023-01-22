import argparse


class ArgumentParser:
    def __init__(self) -> None:
        desc = """Plot kanban diagrams."""
        self.parser = argparse.ArgumentParser(description=desc)
        self.parser.add_argument("filename", help="path to the csv data file")

    def parse(self):
        return self.parser.parse_args()
