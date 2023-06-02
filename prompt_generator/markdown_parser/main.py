import os
import re

from prompt_generator.utils import FileUtils, PrintUtils


def parse_links(content, base_path):
    """Parses links within the content."""
    links = re.findall(r'\[(.*?)]\((.*?)\)', content)

    for file_label, file_path in links:
        full_file_path = os.path.join(base_path, file_path)

        if os.path.isfile(full_file_path):
            content = replace_link_with_content(
                content, file_label, file_path, full_file_path)

    return content


def replace_link_with_content(content, file_label, file_path, full_file_path):
    """Replaces link with its corresponding content."""
    _, file_extension = os.path.splitext(full_file_path)

    if file_extension == '.md':
        file_content = parse_content(full_file_path)
        content = content.replace(
            f'[{file_label}]({file_path})', f'{file_content}')
    else:
        content = content.replace(
            f'[{file_label}]({file_path})', FileUtils.get_code_block(full_file_path, file_label))

    return content


def parse_content(md_file_path):
    """Parses a markdown file, replacing links with the content of the linked files."""
    content = FileUtils.read_file(md_file_path)
    if content:
        content = parse_links(content, os.path.dirname(md_file_path))
    return content


def main(args):
    """Main function to parse markdown file."""
    result = parse_content(args.md_file_path)
    if result:
        PrintUtils.print_result(result, "Parsed Markdown:")
