# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]


---
## [0.2.0] - 2025-07-09

### Added
- data -> data transport & protocols -> real-time messaging protocols
- data -> data transport & protocols -> data marshalling & ipc formats
- data -> data transport & protocols -> bit-encoding formats
- data -> data transport & protocols -> data subscription & publication models
- data -> data integrity & validation -> checksums & hashing
- data -> data integrity & validation -> data validation schemas & rules engines
- data -> data integrity & validation -> error detection & correctioncodes
- data -> data integrity & validation -> in-memory & volatile data
- data -> data integrity & validation -> shared memory segments
- data -> data integrity & validation -> in-process data stores
- data -> data integrity & validation -> volatile configuration & status registers
- platform -> compute -> hardware accel.
- platform -> networking -> real-time & hpc interconnects
- platform -> orchestration & management -> container orchestration
- platform -> orchestration & management -> infrastructure provisioning & IaC
- platform -> orchestration & management -> cluster management
- platform -> system startup & firmware -> bootloaders
- platform -> system startup & firmware -> device drivers
- platform -> system startup & firmware -> firmware update agents
- examples of in-mem and volitile data
- descriptions and examples for all sections and items
- cut divisions to single character
- general division
- iot hub example docs

### Fixed
- Cut Division code to 1 alpha characters for compactness + readability

## [0.1.1] - 2025-07-02

### Added
- CC BY 4.0 license
- Txt and toml export to compiler.py

### Fixed
- scindex code item id for Anomaly & Threat Detection
- typo in changlog

## [0.1.0] - 2025-07-02

### Added
- Initial creation of the Software Component Index (`scindex`).
- Identified six divisions (`DATA`, `PLAT`, `SRVC`, `CORE`, `IFAC`, `DIST`).
- `compiler.py` script for exporting the index to JSON and TOML.
- GitHub repository structure including issue templates and `CONTRIBUTING.md`.

[unreleased]: https://github.com/scindex/scindex/compare/v0.1.1...HEAD
[0.1.0]: https://github.com/scindex/scindex/releases/tag/v0.1.1
[0.1.0]: https://github.com/scindex/scindex/releases/tag/v0.1.0