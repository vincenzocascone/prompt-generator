from .print_utils import TerminalColor, PrintUtils


class InputUtils:
    @staticmethod
    def color_input(text: str, color: TerminalColor = TerminalColor.GREEN, optional: bool = False):
        """Helper function to input colorized text."""
        if optional:
            return input(f"\n{color}{text} (optional): {TerminalColor.END}")
        else:
            return input(f"\n{color}{text}{TerminalColor.END}")

    @staticmethod
    def yes_no_input(text: str, color: TerminalColor = TerminalColor.GREEN):
        """
        Function to handle yes/no input in a way that's not case-sensitive and only accepts valid inputs.
        'Yes' is the default option.
        """
        while True:
            choice = InputUtils.color_input(text, color).lower()
            if choice in ['yes', 'y', '']:
                return True
            elif choice in ['no', 'n']:
                return False
            else:
                PrintUtils.print_color("Please respond with 'yes' or 'no' (or 'y' or 'n').", color)

    @staticmethod
    def file_list_input(color: TerminalColor = TerminalColor.GREEN):
        """Get multiple file paths and corresponding names from the user."""
        files = []
        while True:
            path = InputUtils.color_input("Enter a file path (or press Enter to finish): ", color)
            if path:
                label = InputUtils.color_input("Provide a label for this file",
                                               optional=True)
                file = {'path': path}
                if label:
                    file['label'] = label
                files.append(file)
            else:
                break
        return files
