# Prompt Generator

Prompt Generator is a flexible and user-friendly package that offers customizable scripts for generating effective and
context-aware prompts. These prompts can be used to guide the writing, improvement, and debugging of code.

## Installation

Prompt Generator can be installed easily using pip, a package installer for Python:

```bash
pip install prompt-generator
```

## Features

- ### Generate Docs

  This script generates a prompt that can be used to make the AI write documentation
  for the project. When executed, it will first ask for some info about the project, such as the name, description, root
  path. Optionally you can provide the path to config files such as pyproject.toml for a python project or
  package.json for a node project. The same can be done with particularly relevant files. This will allow the AI to have
  a better understanding of the project and generate more accurate documentation.

  To utilize it, use the following command in your terminal:

    ```bash
    generate_docs
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
  parse_md <path to the markdown file>
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
  get_directory_structure <path to the directory> [-gitignore]
  ```

  Upon successful execution, the resultant json will be displayed in your terminal and copied to your
  clipboard for immediate use or future reference.
