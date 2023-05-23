from print_utils import TerminalColor


def input_color(text: str, color: str = TerminalColor.GREEN):
    """Helper function to input colorized text."""
    return input(f"\n{color}{text}{TerminalColor.END}")
