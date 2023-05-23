from print_utils import print_color, TerminalColor


def read_file(file_path):
    """Reads a file and returns its content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except IOError:
        print_color(f"Failed to open {file_path}", TerminalColor.WARNING)
