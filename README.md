# Software Component Index (“scindex”)

The Software Component Index ("SCIndex", pronounced **IPA: /ˈsɪndeks/** or SIN-deks) is a vendor-neutral, open-standard specification for categorizing and numbering all components of a software system.

To address the software industry's lack of a standard identifier system the Scindex provides a universal indexing system for documenting software projects. Scindex codes are human and machine readable, comparable across products, scalable, robustly traceable, and fit for operationalized uses such as linting, auto-lookup, and AI context setting. Inspired by the AEC industry's "[MasterFormat](https://en.wikipedia.org/wiki/MasterFormat)," Scindex creates a common language that brings immediate clarity to the scope and context of records, enabling improved analysis and interoperability across teams and tools.

## Usage

Scindex provides a structured core identifier that can be flexibly prefixed and suffixed to meet various documentation needs.

The full pattern is: `[PREFIX]-[Scindex Code]-[SUFFIX]`

See the examples directory for sample document sets that make use of scindex-based IDs.

---

### **Core Concept: The Scindex Code**

The **Scindex Code** is the basis of the system, pinpointing a specific category within the software architecture by concatenating three parts:

* **Division (`D`):** An alphabetic character code representing a major architectural area.
* **Section (`01`):** A two-digit code for a section within the division.
* **Item (`40`):** A two-digit code for a specific component type within the section.

For example, the Scindex Code for "Graph Databases" is `D0140`.

---

### **Building a Full Identifier**

You create a complete, unique ID by adding a prefix and a suffix to the Scindex Code.

* **Prefix (Optional):** Identifies the *type* of record. This allows you to manage requirements, decisions, and tests all within the same numbering system.
    * `REQ`: Requirement
    * `ADR`: Architecture Decision Record
    * `TEST`: Test Case
* **Suffix (Required):** A unique ID for the specific record within that category.

#### **Example 1: Architecture Decision**

An ID of **`ADR-D0140-32`** is broken down as:

* `ADR`: This is an Architecture Decision Record.
* `D0140`: The decision relates to "Graph Databases  (`D` -> Data Management, `01` -> Databases, `40` -> Graph Databases)"
* `32`: It's the 32nd decision logged for this category.

#### **Example 2: Requirement**

An ID of `REQ-S0210-5` is broken down as:

* `REQ`: This is a Requirement.
* `S0210`: The requirement relates to "Logging" (`S` -> System Services, `02` -> Observability, `10` -> Logging).
* `5`: It's the 5th requirement defined for the logging category.

---

### **Flexibility in Practice**

The system is designed to be adaptable.

* **Omitting the Prefix:** If your document collection *only* contains requirements, you can omit the `REQ-` prefix for brevity (e.g., `D0140-32`).
* **Flexible Suffixes:** While simple integers are recommended, the suffix can be any format that suits your project's needs, such as `-1a`, `-v2`, `-3.2` or `-20250716`.

This flexibility makes searching and filtering straightforward. For instance, `grep "ADR-D"` would find all architectural decisions related to the data division in documents and source code comments and tags.

## Key Features

* **Human-Readable:** The codes are designed to be quickly understood by people. The use of alphabetic **Division codes** (e.g., `D`, `S`) provides immediate context without implying a rigid order, while the numeric components are easy to scan.

* **Sayable:** The structure is meant to be spoken easily in conversations. For example, the code `D0140` is simply said as "data one-forty," or "data one-forty" which simplifies communication between team members.

* **Predictable Structure:** The standard `[DIVISION][SECTION][ITEM]` format (e.g., `D0140`) has a consistent length, which makes it reliable for automated parsing, pattern-based validation, and use in other tooling.

* **Hierarchical, Scalable & Stable:** The system is inherently hierarchical, reflecting how software components are often organized. New divisions, sections, and items can be added without needing to re-number existing codes.

* **Logical Grouping:** Using a standard count for **Sections** and a "10-series" for **Item codes** (e.g., `10`, `20`, `30`) creates clear, high-level groupings within a section and makes section ids discernibly different from item ids. This provides a logical structure while still allowing for numbers in between (e.g., `11`, `12`) if more granular items need to be added later.

## Releases & Downloads

The Scindex project uses semantic versioning (e.g., `v1.0.0`). Official versions are managed through tagged **GitHub Releases**.

Each release includes the complete index in several convenient formats:
* **YAML** (`scindex.yaml`)
* **JSON** (`scindex.json`)
* **TOML** (`scindex.toml`)

To get the latest version, please visit the official **[Releases Page](https://github.com/scindex/scindex/releases)**, where you can download the files for the version you need.

---
Scindex is joyously ❤️ and meticulously 🧐 maintained by [F39](https://www.f39.design/)



