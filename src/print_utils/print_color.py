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


def print_color(text: str, color: str):
    """Helper function to print colorized text."""
    print(f"\n{color}{text}{TerminalColor.END}\n")
