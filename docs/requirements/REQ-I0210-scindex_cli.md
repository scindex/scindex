---
id: req-I0210-scindex-cli
date: 2025-11-07
summary: Defines requirements for installing and using the Scindex CLI
state: Proposed
tags:
---

# REQ-I0210-scindex-cli: CLI Installation and Usage

## User Story
As a software developer, I want to install the scindex CLI and use it to compile the `scindex.yaml` specification in order to generate various output formats for consumption in my projects.

## Background

The Scindex standard is defined in a canonical `scindex.yaml` file. To make the standard useful, a command-line tool is required to convert this YAML file into other formats like JSON, Markdown, and vector embeddings. This document specifies the requirements for the installation and basic use of this command-line compiler.

## Requirements

1. The `scindex` project MUST be installable as a package from the project root via `pip`.
2. Upon installation, a `scindex` executable command MUST be available in the system's path.
3. The CLI MUST provide a `compile` subcommand (e.g., `scindex compile`) to generate distributable files from the `scindex.yaml` source.
4. The `compile` command MUST, by default, read from a `scindex.yaml` file in the current working directory.
5. The `compile` command, when run with no arguments, MUST generate `scindex.json`, `scindex.toml`, `scindex.txt`, and `scindex.md`.
6. All generated files MUST be placed in a `./dist` directory, which should be created if it does not exist.
7. The `compile` command MUST accept a `--format` option that takes a single format type as an argument.
8. The supported formats for the `--format` option MUST be `json`, `toml`, `txt`, `md`, and `embeddings`.
9. When the `--format` option is used, the command MUST generate only the specified file.

## Acceptance Criteria

AC1: Standard Installation
* **GIVEN** a user has cloned the project repository
* **WHEN** the user runs `pip install .` in the project root
* **THEN** they can run `scindex --version` and see a version number.

AC2: Default Compilation
* **GIVEN** the CLI is installed and a valid `scindex.yaml` is in the current directory
* **WHEN** the user runs `scindex compile`
* **THEN** the files `scindex.json`, `scindex.toml`, `scindex.txt`, and `scindex.md` are created or updated in the `./dist` directory.

AC3: Single Format Compilation
* **GIVEN** the CLI is installed and a valid `scindex.yaml` is in the current directory
* **WHEN** the user runs `scindex compile --format json`
* **THEN** only the `scindex.json` file is created or updated in the `./dist` directory.

AC4: Embeddings Compilation
* **GIVEN** the CLI is installed and a valid `scindex.yaml` is in the current directory
* **WHEN** the user runs `scindex compile --format embeddings`
* **THEN** only the `scindex.embeddings.json` file is created or updated in the `./dist` directory.
