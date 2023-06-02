import json
import os

from prompt_generator.utils import FileUtils, InputUtils, PrintUtils, TerminalColor


# Example of a JSON config file:
# {
#   "name": "Prompt Generator",
#   "description": "Prompt Generator is a flexible and user-friendly package that offers customizable scripts for generating effective and context-aware prompts. These prompts can be used to guide the writing, improvement, and debugging of code.",
#   "root_dir": ".",
#   "config_files": [
#     {
#       "file_path": "pyproject.toml",
#       "file_label": "Python package config file"
#     }
#   ],
#   "main_files": [
#     {
#       "file_path": "prompt_generator/run.py",
#       "file_label": "Run script"
#     },
#     {
#       "file_path": "prompt_generator/markdown_parser/main.py",
#       "file_label": "Main markdown partsesdafasd f script"
#     },
#     {
#       "file_path": "prompt_generator/docs_generator/main.py"
#     },
#     {
#       "file_path": "prompt_generator/directory_structure/main.py"
#     }
#   ],
#   "docs_specs": "Prova docs specs"
# }


def get_file_paths(prompt):
    """Get multiple file paths and corresponding names from the user."""
    file_paths = []
    while True:
        file_path = InputUtils.input_color(prompt)
        if file_path:
            file_label = InputUtils.input_color("Provide a name for this file (or press Enter to skip): ",
                                                optional=True)
            file_paths.append((file_path, file_label))
        else:
            break
    return file_paths


def get_config_from_json(path):
    """
    Load the config info from a JSON file.
    """
    with open(path, 'r') as f:
        config = json.load(f)
    return config


def get_prompt_config():
    """
    Get the prompt info from the user.
    """
    prompt_config = {}
    PrintUtils.print_color("Provide the following prompt data.", TerminalColor.CYAN)
    prompt_config['name'] = InputUtils.input_color("Project Name: ")
    prompt_config['description'] = InputUtils.input_color("Project Description: ")
    prompt_config['target_audience'] = InputUtils.input_color("Target Audience: ", optional=True)
    prompt_config['detailed_descriptions'] = InputUtils.input_color("Detailed Descriptions of the Modules: ",
                                                                    optional=True)
    prompt_config['root_dir'] = InputUtils.input_color("Root Directory Path: ")
    if InputUtils.input_color("Do you want to provide any config/dependencies files? (Y/n): ").lower() not in ['n',
                                                                                                               'no']:
        prompt_config['config_files'] = get_file_paths(
            "Enter a config/dependencies file path (or press Enter to finish): ")
    if InputUtils.input_color("Do you want to provide any important files? (Y/n): ").lower() not in ['n', 'no']:
        prompt_config['main_files'] = get_file_paths("Enter an important file path (or press Enter to finish): ")
    prompt_config['docs_specs'] = InputUtils.input_color("Describe how the documentation should be: ", optional=True)
    return prompt_config


def generate_prompt_markdown(prompt_config):
    """Generate the prompt markdown."""
    # Start with the task
    markdown = "Using the information provided below, create a comprehensive project documentation.\n\n"

    # Add project name and description
    markdown += f"# {prompt_config['name']}\n\n"
    markdown += f"{prompt_config['description']}\n\n"

    # Add the target audience and detailed descriptions if they exist
    if 'target_audience' in prompt_config and prompt_config['target_audience']:
        markdown += f"## Target Audience\n\n{prompt_config['target_audience']}\n\n"

    if 'detailed_descriptions' in prompt_config and prompt_config['detailed_descriptions']:
        markdown += f"## Detailed Descriptions of the Modules\n\n{prompt_config['detailed_descriptions']}\n\n"

    # Add the project structure
    gitignore = FileUtils.load_gitignore(prompt_config['root_dir'])
    markdown += "## Project Structure\n\n"
    markdown += f"```json\n{FileUtils.get_dir_json(prompt_config['root_dir'], gitignore)}\n```\n\n"

    # If there are config files, add them
    if 'config_files' in prompt_config and prompt_config['config_files']:
        markdown += "## Config Files\n\n"
        for file in prompt_config['config_files']:
            file_path = file['file_path']
            file_label = file.get('file_label', None)
            markdown += f"- {FileUtils.get_code_block(file_path, file_label)}\n\n"

    # If there are important files, add them
    if 'main_files' in prompt_config and prompt_config['main_files']:
        markdown += "## Important Files\n\n"
        for file in prompt_config['main_files']:
            file_path = file['file_path']
            file_label = file.get('file_label', None)
            markdown += f"- {FileUtils.get_code_block(file_path, file_label)}\n\n"

    # Add the docs specs if they exist
    if 'docs_specs' in prompt_config and prompt_config['docs_specs']:
        markdown += "## Documentation Specs\n"
        markdown += f"\n{prompt_config['docs_specs']}\n"

    return markdown


def main(args=None):
    if args and args.config and os.path.isfile(args.config):
        prompt_config = get_config_from_json(args.config)
    else:
        prompt_config = get_prompt_config()

    prompt_markdown = generate_prompt_markdown(prompt_config)

    PrintUtils.print_result(prompt_markdown)
