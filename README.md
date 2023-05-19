# Prompt Generator

Prompt Generator is a flexible and user-friendly package that offers customizable scripts for generating meaningful and context-aware prompts. These prompts can be used to guide the writing, enhancement, and debugging of code.

## Installation

Prompt Generator can be installed easily using pip, a package installer for Python:

```bash
pip install prompt-generator
```

## Features

- ### Markdown Parser

  The Markdown Parser is a robust utility specifically designed to parse markdown files. It works by replacing all hyperlinks within a markdown document with the actual content of the linked files. This function proves extremely useful if you maintain a collection of prompt files written in markdown format, and these files contain references to other project documents.

  To utilize the Markdown Parser, use the following command in your terminal:

  ```bash
  parse_md <path to your markdown file>
  ```

  Upon successful execution, the resultant parsed content will be displayed in your terminal. As an added convenience, this content is also automatically copied to your clipboard for immediate use or future reference.
