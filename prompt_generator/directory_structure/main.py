import argparse
import os

from prompt_generator.utils import FileUtils, PrintUtils


def get_args():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser(description="Get directory structure of a project.")
    parser.add_argument("root_dir", type=str, help="Root directory of the project.")
    parser.add_argument("--gitignore", type=str, help="Path to the .gitignore file.", default=None)
    return parser.parse_args()


def main(args):
    """Main function of the directory structure."""
    root_dir = args.root_dir
    gitignore_path = args.gitignore

    if not os.path.isdir(root_dir):
        PrintUtils.print_error("The specified root directory does not exist.")
        return

    gitignore = FileUtils.load_gitignore(root_dir, gitignore_path)
    dir_structure = FileUtils.get_dir_json(root_dir, gitignore)
    PrintUtils.print_result(dir_structure, "Directory Structure:")


if __name__ == "__main__":
    main()
