import pyperclip

from .print_color import print_color, TerminalColor


def print_result(result: str, title: str = "Result"):
    """Helper function to print the result."""
    print_color(title, TerminalColor.HEADER)
    print(result)

    # Copy the result to the clipboard
    pyperclip.copy(result)
    print_color("The result has been copied to the clipboard!",
                f"{TerminalColor.BLUE}{TerminalColor.BOLD}")
