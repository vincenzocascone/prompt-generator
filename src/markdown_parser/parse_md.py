import argparse
import os
import re

from print_utils import print_result, print_color, TerminalColor


def read_file(file_path):
    """Reads a file and returns its content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except IOError:
        print_color(f"Failed to open {file_path}", TerminalColor.WARNING)


def parse_links(content, base_path):
    """Parses links within the content."""
    links = re.findall(r'\[(.*?)]\((.*?)\)', content)

    for text, file_path in links:
        full_file_path = os.path.join(base_path, file_path)

        if os.path.isfile(full_file_path):
            content = replace_link_with_content(
                content, text, file_path, full_file_path)

    return content


def replace_link_with_content(content, text, file_path, full_file_path):
    """Replaces link with its corresponding content."""
    file_content = read_file(full_file_path)
    _, file_extension = os.path.splitext(full_file_path)

    if file_extension == '.md':
        file_content = parse_content(full_file_path)
        content = content.replace(
            f'[{text}]({file_path})', f'{file_content}')
    else:
        content = content.replace(
            f'[{text}]({file_path})', f'```{file_extension[1:]}\n{file_content}\n```')

    return content


def parse_content(md_file_path):
    """Parses a markdown file, replacing links with the content of the linked files."""
    content = read_file(md_file_path)
    if content:
        content = parse_links(content, os.path.dirname(md_file_path))
    return content


def get_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Markdown File Parser")
    parser.add_argument(
        "md_file_path", help="path to the markdown file", type=str)
    return parser.parse_args()


def main():
    """Main function to parse markdown file."""
    args = get_args()
    result = parse_content(args.md_file_path)
    if result:
        print_result(result, "Parsed Markdown:")


if __name__ == "__main__":
    main()