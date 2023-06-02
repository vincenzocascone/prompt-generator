import argparse

from .docs_prompt_generator import main as docs_prompt_generator_main
from .get_dir_structure import main as get_dir_structure_main
from .markdown_parser import main as parse_md_main
from .tasks_prompt_generator import main as tasks_prompt_generator_main


def get_args():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser(description="Prompt Generator")
    subparsers = parser.add_subparsers(dest="command")

    parser_docs_prompt = subparsers.add_parser("docs_prompt",
                                               help="Generate a prompt that can be useful to create docs for the "
                                                    "project.")
    parser_docs_prompt.add_argument('-c', '--config', type=str,
                                    help="Path to a JSON file containing the prompt config.")

    parser_task_generator = subparsers.add_parser("tasks_prompt", help="Generate a prompt that can be useful to "
                                                                       "complete specific tasks.")
    parser_task_generator.add_argument('-c', '--config', type=str,
                                       help="Path to a JSON file containing the prompt config.")

    parser_get_dir_json = subparsers.add_parser("get_dir_structure",
                                                help="Get a directory's structure as a JSON object.")
    parser_get_dir_json.add_argument("root_dir", type=str, help="Directory path.")
    parser_get_dir_json.add_argument("-g", "--gitignore", type=str, help="Path to the .gitignore file.",
                                     default=None)

    parser_parse_md = subparsers.add_parser("parse_md",
                                            help="Parse markdown file, replacing links with the content of the "
                                                 "linked files.")
    parser_parse_md.add_argument("md_file_path", type=str, help="Path to the markdown file to parse.")

    return parser.parse_args()


def main():
    """Main function of the prompt generator."""
    args = get_args()

    if args.command == "docs_prompt":
        docs_prompt_generator_main(args)
    elif args.command == "tasks_prompt":
        tasks_prompt_generator_main(args)
    elif args.command == "get_dir_structure":
        get_dir_structure_main(args)
    elif args.command == "parse_md":
        parse_md_main(args)
    else:
        print("Unknown command. Use --help for more information.")


if __name__ == "__main__":
    main()
