import os

from file_utils.read_file import read_file


def get_code_block(file_path):
    """Get the code block for a file."""
    file_content = read_file(file_path)
    _, file_extension = os.path.splitext(file_path)
    file_name = os.path.basename(file_path)
    return f"{file_name}:\n```{file_extension[1:]}\n{file_content}\n```"
