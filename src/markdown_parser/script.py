import os
import re
import argparse
import pyperclip


class TerminalColor:
    """Class containing ANSI escape sequences for terminal colors and styles."""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def read_file(file_path):
    """Reads a file and returns its content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except IOError:
        print(f"{TerminalColor.WARNING}Failed to open {file_path}{TerminalColor.ENDC}")
        return ""


def parse_content(md_file_path):
    """Parses a markdown file, replacing links with the content of the linked files."""
    # Read the markdown file
    content = read_file(md_file_path)

    # Find all markdown links in the file
    links = re.findall(r'\[(.*?)\]\((.*?)\)', content)

    # Iterate over all links
    for link in links:
        text, file_path = link
        full_file_path = os.path.realpath(os.path.join(
            os.path.dirname(md_file_path), file_path))

        # Check if file exists
        if os.path.isfile(full_file_path):
            file_content = read_file(full_file_path)
            _, file_extension = os.path.splitext(full_file_path)

           # If the linked file is a markdown file, parse it as well
            if file_extension == '.md':
                file_content = parse_content(full_file_path)
                content = content.replace(
                    f'[{text}]({file_path})', f'{file_content}')
            else:
                # Replace the markdown link with the file content in a code block
                content = content.replace(
                    f'[{text}]({file_path})', f'```{file_extension[1:]}\n{file_content}\n```')

    return content


def main():
    """Main function to parse markdown file."""
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description="Markdown File Parser")
    parser.add_argument(
        "md_file_path", help="path to the markdown file", type=str)
    args = parser.parse_args()

    # Use the function and print the result
    result = parse_content(args.md_file_path)

    if result:
        print(
            f"\n{TerminalColor.HEADER}{TerminalColor.BOLD}Parsed content:{TerminalColor.ENDC}\n")
        print(result)

        # Copy the result to the clipboard
        pyperclip.copy(result)
        print(
            f"\n{TerminalColor.OKBLUE}{TerminalColor.BOLD}Result has been copied to the clipboard!{TerminalColor.ENDC}\n")


if __name__ == "__main__":
    main()
