import json
import os

from prompt_generator.utils import FileUtils, InputUtils, PrintUtils, TerminalColor


def get_file_paths(prompt):
    """Get multiple file paths from the user."""
    file_paths = []
    while True:
        file_path = InputUtils.input_color(prompt)
        if file_path:
            file_paths.append(file_path)
        else:
            break
    return file_paths


def get_config_from_json(path):
    """
    Load the config info from a JSON file.
    """
    with open(path, 'r') as f:
        project_info = json.load(f)
    return project_info


def get_project_info():
    """
    Get the project info from the user.
    Name, Description, Root Directory Path, Config/Dependencies file/files, Project Structure, Important Files
    """
    project_info = {}
    PrintUtils.print_color("Provide the following project data.", TerminalColor.CYAN)
    project_info['name'] = InputUtils.input_color("Project Name: ")
    project_info['description'] = InputUtils.input_color("Project Description: ")
    project_info['root_dir'] = InputUtils.input_color("Root Directory Path: ")
    if InputUtils.input_color("Do you want to provide any config/dependencies files? (Y/n): ").lower() not in ['n',
                                                                                                               'no']:
        project_info['config_files'] = get_file_paths(
            "Enter a config/dependencies file path (or press Enter to finish): ")
    if InputUtils.input_color("Do you want to provide any important files? (Y/n): ").lower() not in ['n', 'no']:
        project_info['main_files'] = get_file_paths("Enter an important file path (or press Enter to finish): ")
    return project_info


def get_docs_info():
    """
    Get the docs info from the user.
    """
    docs_info = InputUtils.input_color("Describe how the documentation should be (or press Enter to finish): ")

    return docs_info


def generate_prompt_markdown(project_info, docs_info=None):
    """Generate the prompt markdown."""
    # Start with the task
    markdown = "The following data describes a project, based on that write a documentation using Markdown syntax.\n\n"

    # Add project name
    markdown += f"# {project_info['name']}\n\n"

    # Add the project description
    markdown += f"{project_info['description']}\n\n"

    # Add the project structure
    gitignore = FileUtils.load_gitignore(project_info['root_dir'])
    markdown += "## Project Structure\n\n"
    markdown += f"```json\n{FileUtils.get_dir_json(project_info['root_dir'], gitignore)}\n```\n\n"

    # If there are config files, add them
    if 'config_files' in project_info:
        markdown += "## Config Files\n\n"
        for file_path in project_info['config_files']:
            markdown += f"- {FileUtils.get_code_block(file_path)}\n\n"

    # If there are important files, add them
    if 'main_files' in project_info:
        markdown += "## Important Files\n\n"
        for file_path in project_info['main_files']:
            markdown += f"- {FileUtils.get_code_block(file_path)}\n\n"

    # Add the docs info
    if docs_info:
        markdown += "## Documentation Specs\n"
        markdown += f"\n{docs_info}\n"

    return markdown


def main(args=None):
    if args and args.config and os.path.isfile(args.config):
        config = get_config_from_json(args.config)
        project_info = config.get('project_info', None)
        docs_info = config.get('docs_info', None)
    else:
        project_info = get_project_info()
        docs_info = get_docs_info()

    prompt_markdown = generate_prompt_markdown(project_info, docs_info)

    PrintUtils.print_result(prompt_markdown)
