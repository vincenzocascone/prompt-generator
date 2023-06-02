import os

from prompt_generator.utils import FileUtils, InputUtils, PrintUtils, TerminalColor


def get_user_input():
    """
    Get the user input for the prompt.
    """
    prompt_config = {}
    PrintUtils.print_color("Provide the following data in order to generate the prompt",
                           TerminalColor.CYAN)

    if InputUtils.yes_no_input(
            "Do you have a README/docs file that contains an overall explanation of the project? (Y/n): "):
        prompt_config['docs_path'] = InputUtils.color_input("File path: ")
    else:
        prompt_config['project_overview'] = InputUtils.color_input("Provide an overview of the project: ")

    if InputUtils.yes_no_input("Do you want to provide any files related to the tasks? (Y/n): "):
        prompt_config['relevant_files'] = InputUtils.file_list_input()

    PrintUtils.print_color("Now write the tasks",
                           TerminalColor.CYAN)

    prompt_config['tasks'] = []
    while True:
        task = InputUtils.color_input("Enter the task (or press Enter to finish): ")
        if not task:
            break
        prompt_config['tasks'].append(task)

    return prompt_config


def generate_prompt_markdown(prompt_config):
    """Generate the tasks prompt markdown."""

    markdown = "Using the information provided below, accomplish the following tasks for the project.\n\n"

    markdown += "## Tasks\n\n"
    for i, task in enumerate(prompt_config['tasks']):
        markdown += f"{i + 1}. {task}\n\n"

    if 'docs_path' in prompt_config and prompt_config['docs_path']:
        markdown += f"{FileUtils.read_file(prompt_config['docs_path'])}\n\n"
    elif 'project_overview' in prompt_config and prompt_config['project_overview']:
        markdown += f"# Project Overview\n\n{prompt_config['project_overview']}\n\n"

    if 'relevant_files' in prompt_config and prompt_config['relevant_files']:
        markdown += FileUtils.get_files_list("## Relevant Files\n\n", prompt_config['relevant_files'])

    return markdown


def main(args=None):
    prompt_config = FileUtils.get_config_from_json(args.config) if args and args.config and os.path.isfile(
        args.config) else get_user_input()

    if prompt_config is None:
        PrintUtils.print_color("Cannot proceed without a valid configuration.", TerminalColor.BLUE)
        return

    prompt_markdown = generate_prompt_markdown(prompt_config)
    PrintUtils.print_result(prompt_markdown)
