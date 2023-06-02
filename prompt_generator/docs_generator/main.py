import os

from prompt_generator.utils import FileUtils, InputUtils, PrintUtils, TerminalColor


def get_user_input():
    """
    Get the user input for the prompt.
    """
    config = {}
    PrintUtils.print_color("Provide the following prompt data.", TerminalColor.CYAN)
    config['name'] = InputUtils.color_input("Project Name: ")
    config['description'] = InputUtils.color_input("Project Description: ")
    config['target_audience'] = InputUtils.color_input("Target Audience", optional=True)
    config['root_dir'] = InputUtils.color_input("Root Directory Path: ")

    if InputUtils.yes_no_input("Do you want to provide any config/dependencies files? (Y/n): "):
        config['config_files'] = InputUtils.file_list_input()
    if InputUtils.yes_no_input("Do you want to provide any important files? (Y/n): "):
        config['main_files'] = InputUtils.file_list_input()
    config['docs_specs'] = InputUtils.color_input("Describe how the documentation should be: ", optional=True)
    return config


def generate_prompt_markdown(prompt_config):
    """Generate the prompt markdown."""

    markdown = "Using the information provided below, create a comprehensive project documentation.\n\n"
    markdown += f"# {prompt_config['name']}\n\n"
    markdown += f"{prompt_config['description']}\n\n"

    if 'target_audience' in prompt_config and prompt_config['target_audience']:
        markdown += f"## Target Audience\n\n{prompt_config['target_audience']}\n\n"

    gitignore = FileUtils.load_gitignore(prompt_config['root_dir'])
    markdown += "## Project Structure\n\n"
    markdown += f"```json\n{FileUtils.get_dir_json(prompt_config['root_dir'], gitignore)}\n```\n\n"

    if 'config_files' in prompt_config and prompt_config['config_files']:
        markdown += FileUtils.get_files_list("## Config Files\n\n", prompt_config['config_files'])
    if 'main_files' in prompt_config and prompt_config['main_files']:
        markdown += FileUtils.get_files_list("## Important Files\n\n", prompt_config['main_files'])

    if 'docs_specs' in prompt_config and prompt_config['docs_specs']:
        markdown += "## Documentation Specs\n"
        markdown += f"\n{prompt_config['docs_specs']}\n"

    return markdown


def main(args=None):
    prompt_config = FileUtils.get_config_from_json(args.config) if args and args.config and os.path.isfile(
        args.config) else get_user_input()

    if prompt_config is None:
        PrintUtils.print_color("Cannot proceed without a valid configuration.", TerminalColor.BLUE)
        return

    prompt_markdown = generate_prompt_markdown(prompt_config)
    PrintUtils.print_result(prompt_markdown)
