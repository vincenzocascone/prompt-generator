# Prompt Generator

Prompt Generator is a flexible and user-friendly package that offers customizable scripts for generating effective and
context-aware prompts. These prompts can be used to guide the writing, improvement, and debugging of code.

## Installation

Prompt Generator can be installed easily using pip, a package installer for Python:

```bash
pip install prompt-generator
```

## Features

- ### Generate Project Documentation

  This script generates a prompt that can be used to make the AI write documentation for the project.

  When executed without arguments it will ask for some info about the project, such as the name, description, root
  directory, paths to config files, main files, and docs specs.

  Instead of writing the info manually you can also provide the path to a JSON file that contains the prompt
  configuration.
  The JSON should have the following structure:

  ```
  {
    "name": "<string> (required)",
    "description": "<string> (required)",
    "target_audience": "<string> (optional)",
    "root_dir": "<string> (required)",
    "config_files": [
        {
            "path": "<string> (required)",
            "label": "<string> (optional)"
        },
        ...
    ] (optional),
    "main_files": [
        {
            "path": "<string> (required)",
            "label": "<string> (optional)"
        },
        ...
    ] (optional),
    "docs_specs": "<string> (optional)"
  }
  ```

  To utilize this script, use the following command in your terminal:

  ```bash
  pg docs_prompt [--config <path to config file>]
  ```

  Upon successful execution, the resultant prompt will be displayed in your terminal and copied to your clipboard for
  immediate use or future reference.

- ### Complete Tasks

  This script generates a prompt that can be used to help AI complete tasks for the project.

  It will ask for the project name, description or the path to README/docs, root directory, and optionally the paths and
  labels to the files related to the tasks. Finally, it will ask for the single task or task list.

  The JSON should have the following structure:

  ```
  {
    "project_overview": "<string> (optional)",
    "docs_path": "<string> (optional)",
    "relevant_files": [
      {
        "path": "<string> (required)",
        "label": "<string> (optional)"
      },
      ...
    ] (optional),
    "tasks": [
      "<string> (required)",
      ...
    ] (required)
  }
  ```

  To utilize this script, use the following command in your terminal:

  ```bash
  pg tasks_prompt [--config <path to config file>]
  ```

  Upon successful execution, the resultant prompt will be displayed in your terminal and copied to your clipboard for
  immediate use or future reference.

- ### Markdown Parser

  The Markdown Parser is a robust utility specifically designed to parse markdown files. It works by replacing all
  hyperlinks within a Markdown document with the actual content of the linked files. This function proves extremely
  useful if you maintain a collection of prompt files written in Markdown format, and these files contain references to
  other project documents.

  To utilize it, use the following command in your terminal:

  ```bash
  pg parse_md <path to the markdown file>
  ```

  Upon successful execution, the resultant parsed content will be displayed in your terminal and copied to your
  clipboard for immediate use or future reference.

- ### Directory Structure

  This tool provides a clear, nested representation of the structure of a directory in your project. It has been
  designed with gitignore compatibility, meaning it will respect the file exclusion rules defined in your project's
  .gitignore file. This makes it an essential tool for giving the AI a better understanding of the context of your
  project. The returned JSON is minified in order to be more token efficient.

  To utilize it, use the following command in your terminal. You can optionally provide the .gitignore file path using
  the -gitignore flag, if not provided, the script will search for a .gitignore file in the root directory:

  ```bash
  pg get_dir_structure <path to the directory> [--gitignore <path to the .gitignore file>]
  ```

  Upon successful execution, the resultant json will be displayed in your terminal and copied to your
  clipboard for immediate use or future reference.
