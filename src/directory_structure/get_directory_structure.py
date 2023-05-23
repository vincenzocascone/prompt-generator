import argparse

from file_utils import get_dir_json, load_gitignore
from print_utils import print_result


def get_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Directory Structure")
    parser.add_argument(
        "root_dir_path", help="path to the root directory", type=str)
    parser.add_argument(
        "-gitignore", help="path to the .gitignore file", type=str, default=None)
    return parser.parse_args()


def main():
    """Main function to get the directory structure."""
    args = get_args()
    gitignore = load_gitignore(args.root_dir_path, args.gitignore)
    result = get_dir_json(args.root_dir_path, gitignore)
    if result:
        print_result(result, "Directory Structure:")


if __name__ == "__main__":
    main()
