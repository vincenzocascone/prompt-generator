from .print_utils import TerminalColor


class InputUtils:
    @staticmethod
    def input_color(text: str, color: str = TerminalColor.GREEN, optional: bool = False):
        """Helper function to input colorized text."""
        if optional:
            return input(f"\n{color}{text}{TerminalColor.END} (optional): ")
        else:
            return input(f"\n{color}{text}{TerminalColor.END}")
