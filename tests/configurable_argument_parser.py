from src.kanban_metrics.argument_parser import ArgumentParser


class ConfigurableArgumentParser(ArgumentParser):

    def __init__(self, filename: str) -> None:
        super().__init__()
        self.args = [filename]

    def parse(self):
        return self.parser.parse_args(self.args)
