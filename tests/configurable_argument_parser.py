from src.kanban_metrics.argument_parser import ArgumentParser


class ConfigurableArgumentParser(ArgumentParser):
    def parse_custom_args(self, cli_arguments):
        return self.parser.parse_args(cli_arguments)
