import argparse

from .directory_structure import main as directory_structure_main
from .docs_generator import main as generate_docs_main
from .markdown_parser import main as markdown_parser_main


def get_args():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser(description="Prompt Generator")
    subparsers = parser.add_subparsers(dest="command")

    parser_generate_docs = subparsers.add_parser("generate_docs", help="Generate docs from project info.")
    parser_generate_docs.add_argument('-c', '--config', type=str,
                                      help="Path to a JSON config file containing the prompt info.")

    parser_directory_structure = subparsers.add_parser("get_directory_structure",
                                                       help="Get directory structure of a project.")
    parser_directory_structure.add_argument("root_dir", type=str, help="Root directory of the project.")
    parser_directory_structure.add_argument("--gitignore", type=str, help="Path to the .gitignore file.", default=None)

    parser_markdown_parser = subparsers.add_parser("parse_md",
                                                   help="Parse markdown file, replacing links with the content of the linked files.")
    parser_markdown_parser.add_argument("md_file_path", type=str, help="Path to the markdown file to parse.")

    return parser.parse_args()


def main():
    """Main function of the prompt generator."""
    args = get_args()

    if args.command == "generate_docs":
        generate_docs_main(args)
    elif args.command == "get_directory_structure":
        directory_structure_main(args)
    elif args.command == "parse_md":
        markdown_parser_main(args)
    else:
        print("Unknown command. Use --help for more information.")


if __name__ == "__main__":
    main()
