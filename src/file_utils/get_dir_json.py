import json
import os
from pathlib import Path


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
