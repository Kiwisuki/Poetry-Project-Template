# Python Project template

## Introduction

Template for Python applications, used for standardized structure within Data Team projects.

## Installation

To setup the project, run the following command:

```bash
make env
```
Afterwards, you can activate the environment by running:

```bash
poetry shell
```

## Building the package

To build the package, run the following command:

```bash
poetry build
```

Or simply commit the changes since pre-commit hook will build the package automatically.

## Structure

```bash
.
├── .gitignore                    # Specifies files to ignore in Git version control
├── .pre-commit-config.yaml       # Configuration file for pre-commit hooks
├── README.md                     # Documentation file for the project
├── makefile                      # Script for automating build tasks
├── pyproject.toml                # Configuration file for Python project
└── src                           # Source code directory
    ├── template_ai_app           # Main application directory
    │   └── addition.py           # Python script for addition functionality
    └── tests                     # Directory for test cases
        └── test_addition.py      # Unit tests for addition.py

```