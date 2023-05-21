import argparse
import json
import os
from pathlib import Path

import pathspec

from print_utils import print_result


def load_gitignore(root_dir, gitignore_path=None):
    """
    Loads the .gitignore file if it exists and returns a pathspec object.
    If gitignore_path is provided, use it. Otherwise, search in the root directory.
    """
    if gitignore_path:
        gitignore_file = Path(gitignore_path)
    else:
        gitignore_file = Path(root_dir) / '.gitignore'

    if gitignore_file.exists():
        with gitignore_file.open('r', encoding='utf-8') as file:
            gitignore = file.read().splitlines()
    else:
        gitignore = []

    return pathspec.PathSpec.from_lines('gitwildmatch', gitignore)


def get_directory_structure(root_dir, gitignore):
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


def main():
    """Main function to get the directory structure."""
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description="Directory Structure")
    parser.add_argument(
        "root_dir_path", help="path to the root directory", type=str)
    parser.add_argument(
        "-gitignore", help="path to the .gitignore file", type=str, default=None)

    args = parser.parse_args()

    # Load the gitignore file if it exists
    gitignore = load_gitignore(args.root_dir_path, args.gitignore)

    # Get the root directory structure
    result = get_directory_structure(args.root_dir_path, gitignore)

    if result:
        print_result(result, "Directory Structure:")


if __name__ == "__main__":
    main()
