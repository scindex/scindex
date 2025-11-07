# Contributing to the Software Component Index (scindex)

Thank you for considering a contribution! Your help is essential for keeping the `scindex` accurate, relevant, and useful for everyone.

This document provides a set of guidelines for contributing to this repository. Following these guidelines helps to communicate that you respect the time of the developers managing this open source project. In return, they should reciprocate that respect in addressing your issue, assessing changes, and helping you finalize your pull requests.

## Code of Conduct

This project and everyone participating in it is governed by the [Contributor Covenant Code of Conduct](https.www.contributor-covenant.org/version/2/1/code_of_conduct.html). By participating, you are expected to uphold this code. Please report unacceptable behavior.

---

## How Can I Contribute?

There are two primary ways to contribute to the index:
* **Suggesting new entries**: Proposing new components or categories that are not yet in the index.
* **Correcting existing entries**: Fixing typos, improving descriptions, or reclassifying an existing entry.

### Your First Contribution

Unsure where to begin? You can start by looking through `needs-review` issues:

* **[Suggestions needing review](https://github.com/scindex/scindex/labels/suggestion)**: These are proposed new entries that need discussion and feedback from the community.
* **[Corrections needing review](https://github.com/scindex/scindex/labels/correction)**: These are proposed fixes that need validation.

### The Contribution Workflow

We follow an **"Issue-first"** workflow. This means that any proposed change must be discussed in an Issue before a Pull Request is opened. This prevents wasted work and ensures that all changes align with the project's direction.

**Step 1: Open an Issue**

* **For a new idea**, use the [**Suggestion**](https://github.com/scindex/scindex/issues/new/choose) issue template.
* **For a mistake in an existing entry**, use the [**Correction**](https://github.com/scindex/scindex/issues/new/choose) issue template.

Please be as detailed as possible in the issue. The maintainers will review the issue and discuss it with you.

**Step 2: Create a Pull Request**

Once the change has been discussed and has received a go-ahead from a maintainer, you are welcome to open a Pull Request.

1.  **Fork the repository** and create a new branch from `main`.
2.  Make your changes in your branch to the **`scindex.yaml`** file only.
    * **Do not** edit the `compiler.py` script unless the issue specifically calls for it.
    * **Do not** run the compiler and commit any of the generated files (`scindex.json`, etc.). These are handled by the maintainers during the release process.
3.  Open a new Pull Request. In the description, be sure to **link the issue** that your PR resolves (e.g., "Fixes #42"). This helps us track the history of every change.
4.  A maintainer will review your Pull Request. If any changes are needed, we will work with you to get it ready for merging.

Once your Pull Request is merged, your contribution will be included in the next official release! Thank you for making the `scindex` better.

---

## Development Environment and Tooling

If you are contributing to the Python tooling for this project, follow these instructions to set up your development environment.

### 1. Prerequisites
*   Python 3.8 or higher.
*   `pip` and `venv` for package management.

### 2. Environment Setup
First, clone the repository to your local machine. Then, from the root of the project directory, create and activate a virtual environment:

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On macOS and Linux:
source .venv/bin/activate
# On Windows:
# .\.venv\Scripts\activate
```

### 3. Install Dependencies
With your virtual environment activated, install the project in "editable" mode. This will install all required dependencies and create the `scindex` command-line tool linked directly to your source code.

```bash
pip install -e .
```

After installation, you can verify that the CLI tool is working:
```bash
scindex --help
```

### 4. Using the CLI Tool
The primary tool for developers is the `scindex` command, which allows you to generate the various distribution formats from the master `scindex.yaml` file.

#### The `export` Command
The `export` command compiles the `scindex.yaml` file into other formats.

**Usage:**
```
scindex export [--dict <path>] [--output <dir>] [--format <name>]
```

**Arguments:**
*   `--dict <path>`: Path to the source `scindex.yaml` file. Defaults to `scindex.yaml` in the current directory.
*   `--output <dir>`: Directory where generated files will be saved. Defaults to `dist/`.
*   `--format <name>`: A specific format to generate (`json`, `toml`, `txt`, `md`, `embeddings`). If omitted, all standard formats (except embeddings) are generated.

**Examples:**

```bash
# Generate all standard formats (json, toml, txt, md) into the dist/ directory
scindex export

# Generate only the JSON output
scindex export --format json

# Generate the Markdown file in a different directory
scindex export --format md --output ./docs/generated

# Generate embeddings from a differently named source file
scindex export --format embeddings --dict ./my-custom-index.yaml
```

### 5. Running Tests
The project uses `pytest` for testing. To run the test suite, execute the following command from the project root:

```bash
pytest
```
This will discover and run all tests located in the `tests/` directory.
