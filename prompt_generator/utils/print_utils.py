import pyperclip


class TerminalColor:
    """Class containing ANSI escape sequences for terminal colors and styles."""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class PrintUtils:
    @staticmethod
    def print_color(text: str, color: str):
        """Helper function to print colorized text."""
        print(f"\n{color}{text}{TerminalColor.END}\n")

    @staticmethod
    def print_result(result: str, title: str = "Result"):
        """Helper function to print the result."""
        PrintUtils.print_color(title, TerminalColor.HEADER)
        print(result)

        # Copy the result to the clipboard
        pyperclip.copy(result)
        PrintUtils.print_color("The result has been copied to the clipboard!",
                               f"{TerminalColor.BLUE}{TerminalColor.BOLD}")
