import json
import os
from pathlib import Path

import pathspec

from .print_utils import PrintUtils, TerminalColor


class FileUtils:
    @staticmethod
    def get_code_block(file_path):
        """Get the code block for a file."""
        file_content = FileUtils.read_file(file_path)
        _, file_extension = os.path.splitext(file_path)
        file_name = os.path.basename(file_path)
        return f"{file_name}:\n```{file_extension[1:]}\n{file_content}\n```"

    @staticmethod
    def get_dir_json(root_dir, gitignore):
        """
        Creates a nested dictionary that represents the folder structure of root_dir
        """
        root = Path(root_dir)
        dir_dict = {'type': 'directory',
                    'name': root.name, 'children': []}

        for dirpath, dirnames, filenames in os.walk(root_dir):
            # Remove dirnames and filenames that match the gitignore rules
            relative_dirpath = Path(dirpath).relative_to(root)
            dirnames[:] = [d for d in dirnames if not gitignore.match_file(
                str(relative_dirpath / d))]
            filenames = [f for f in filenames if not gitignore.match_file(
                str(relative_dirpath / f))]

            # We are interested in the relative path from root_dir
            relative_path = str(Path(dirpath).relative_to(root))
            parent = dir_dict
            if relative_path:
                for dirname in Path(relative_path).parts:
                    for child in parent['children']:
                        if child['name'] == dirname:
                            parent = child
                            break

            # Add directories
            for dirname in dirnames:
                new_dir = {'type': 'directory', 'name': dirname, 'children': []}
                parent['children'].append(new_dir)

            # Add files
            for filename in filenames:
                parent['children'].append({'type': 'file', 'name': filename})

        return json.dumps(dir_dict)

    @staticmethod
    def load_gitignore(root_dir, gitignore_path=None):
        """
        Loads the .gitignore file if it exists and returns a pathspec object.
        If gitignore_path is provided, use it. Otherwise, search in the root directory.
        """
        if gitignore_path:
            gitignore_file = Path(gitignore_path)
        else:
            gitignore_file = Path(root_dir) / '.gitignore'

        gitignore = ['.git/']  # Always ignore .git directory
        if gitignore_file.exists():
            with gitignore_file.open('r', encoding='utf-8') as file:
                gitignore += file.read().splitlines()

        return pathspec.PathSpec.from_lines('gitwildmatch', gitignore)

    @staticmethod
    def read_file(file_path):
        """Reads a file and returns its content."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except IOError:
            PrintUtils.print_color(f"Failed to open {file_path}", TerminalColor.WARNING)
