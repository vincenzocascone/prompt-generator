from file_utils import get_code_block, get_dir_json, load_gitignore
from input_utils import input_color
from print_utils import print_color, print_result, TerminalColor


def get_file_paths(prompt):
    """Get multiple file paths from the user."""
    file_paths = []
    while True:
        file_path = input_color(prompt)
        if file_path:
            file_paths.append(file_path)
        else:
            break
    return file_paths


def get_project_info():
    """
    Get the project info from the user.
    Name, Description, Root Directory Path, Config/Dependencies file/files, Project Structure, Important Files
    """
    project_info = {}
    print_color("Provide the following project data.", TerminalColor.CYAN)
    project_info['name'] = input_color("Project Name: ")
    project_info['description'] = input_color("Project Description: ")
    project_info['rootDir'] = input_color("Root Directory Path: ")
    if input_color("Do you want to provide any config/dependencies files? (Y/n): ").lower() not in ['n', 'no']:
        project_info['configFilePaths'] = get_file_paths(
            "Enter a config/dependencies file path (or press Enter to finish): ")
    if input_color("Do you want to provide any important files? (Y/n): ").lower() not in ['n', 'no']:
        project_info['importantFiles'] = get_file_paths("Enter an important file path (or press Enter to finish): ")
    return project_info


def generate_prompt_markdown(project_info):
    """Generate the prompt markdown."""
    # Start with project name
    markdown = f"# {project_info['name']}\n\n"

    # Add the project description
    markdown += f"{project_info['description']}\n\n"

    # Add the project structure
    gitignore = load_gitignore(project_info['rootDir'])
    markdown += "## Project Structure\n\n"
    markdown += f"```json\n{get_dir_json(project_info['rootDir'], gitignore)}\n```\n\n"

    # If there are config files, add them
    if 'configFilePaths' in project_info:
        markdown += "## Config Files\n\n"
        for file_path in project_info['configFilePaths']:
            markdown += f"- {get_code_block(file_path)}\n\n"

    # If there are important files, add them
    if 'importantFiles' in project_info:
        markdown += "## Important Files\n\n"
        for file_path in project_info['importantFiles']:
            markdown += f"- {get_code_block(file_path)}\n\n"

    # Add the prompt for creating documentation
    markdown += "## Task\n\n"
    markdown += "Based on the provided data write a documentation for this project, the documentation will be written " \
                "as a markdown file and will have at least the following sections: Project overview, " \
                "table of contents, installment, usage, project structure and stack/dependencies.\n"

    return markdown


def main():
    project_info = get_project_info()

    prompt_markdown = generate_prompt_markdown(project_info);

    print_result(prompt_markdown)


if __name__ == '__main__':
    main()
