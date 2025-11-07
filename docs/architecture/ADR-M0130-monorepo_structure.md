---
id: adr-M0130-monorepo-structure
date: 2025-11-07
summary: Adopt a standard src-layout for the Python project to improve scalability and maintainability.
status: Accepted
tags:
---

# ADR-M0130-monorepo-structure: Adopt Standard Python Project Structure

## Context
The project was initiated with tools in a `/tools` directory and other scripts planned for a `/metrics` directory. As the number of tools and scripts is expected to grow, this flat structure would become disorganized and hard to maintain. A scalable, standard, structure was needed to support future growth, testing, and packaging.

## Decision
We will adopt a standard Python "src layout" structure. All core Python source code will be moved into a `/src/scindex` directory, making it a formal Python package. Top-level directories for `/tests`, `/docs`, and `/examples` will be used to clearly separate concerns. Project dependencies and metadata will be managed in a `pyproject.toml` file at the root.

## Consequences
* **Positive**:
    * The project is now a standard, installable Python package.
    * The structure is scalable and familiar to Python developers.
    * There is a clear separation between source code, tests, documentation, and build artifacts.
    * `pyproject.toml` provides a single source of truth for project configuration.
* **Negative**:
    * The file structure is slightly more nested.
    * Developers may need to run `pip install -e .` and/or setup a local virtual environment to contribute to scindex development.
    * The project structure actively skews to toward developers installing/contributing to tht `scindex` python app instead of focusing on the intended audience of program managers, and development leads using the scindex release files as AI context.
