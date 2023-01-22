from src.kanban_metrics.argument_parser import ArgumentParser


class CommandLineArgumentParser(ArgumentParser):
    def __init__(self) -> None:
        super().__init__()

    def parse(self):
        return self.parser.parse()
