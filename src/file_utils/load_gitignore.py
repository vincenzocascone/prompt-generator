from pathlib import Path

import pathspec


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
