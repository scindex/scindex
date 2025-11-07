---
id: req-C0220-evaluation-tool
date: 2025-11-07
summary: A tool to quantitatively score the quality of Scindex categories against a corpus of real-world software components.
state: Proposed
tags:
---

# REQ-C0220-evaluation-tool: Scindex Evaluation Tool

## User Story
As a Scindex maintainer, I want to quantitatively score the coverage and distinctness of Scindex categories in order to objectively evaluate and improve the standard based on real-world software projects.

## Background
The Scindex is a theoretical model for classifying software components. To ensure its real-world relevance, we need a data-driven way to measure how well its categories align with the actual software ecosystem. The methodology is outlined in `???`, based on vector space analysis.

## Requirements

1. The tool MUST load the pre-generated Scindex item vectors from `dist/scindex.embeddings.json`.
2. The tool MUST load a pre-computed corpus of vectors generated from real-world software components (e.g., from npm, PyPI, GitHub).
3. For each Scindex item, the tool MUST calculate a "Coverage Score" (0.0 to 1.0) representing the semantic density of its corresponding real-world component cluster.
4. For each Scindex item, the tool MUST calculate a "Distinctness Score" (0.0 to 1.0) representing its semantic distance from the nearest neighboring Scindex item.
5. The tool MUST calculate a final, weighted score for each item.
6. The tool MUST print a summary report to the console, listing each item with its scores.

## Acceptance Criteria

AC1: Successful Evaluation Run
* **GIVEN** a valid `scindex.embeddings.json` file and a valid corpus vector file are present
* **WHEN** the user executes the evaluation script
* **THEN** the script outputs a list of all Scindex items, each with a calculated Coverage, Distinctness, and Final score.
* **AND** all scores are formatted as floating-point numbers between 0.0 and 1.0.
