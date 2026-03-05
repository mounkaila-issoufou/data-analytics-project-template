# Changelog

All notable changes to this project will be documented in this file.

The format is based on **Keep a Changelog**
https://keepachangelog.com/en/1.0.0/

This project adheres to **Semantic Versioning**
https://semver.org/

---

## [Unreleased]

### Added
- CLI entry point for project scaffolding
- Project scaffolder architecture (`project_scaffolder`)
- Support for generating full data analysis project structures
- Project templates system
- Pre-commit configuration template
- Docker compose template
- Changelog template
- Tests folder generation
- Logging utility for generated projects
- SQL project structure (`analytics`, `ddl`, `dml`, `reset`)

### Changed
- Refactored scaffolding architecture
- Improved configuration management
- Improved README project template
- Improved file generation logic

### Generated Project Improvements
Generated projects now include:

- Structured data directories (`raw`, `processed`, `curated`)
- SQL structure
- Modular Python source structure
- Notebooks workflow
- Dashboard directories (PowerBI / Looker)
- Tests directory
- Logs directory

---

## [0.1.0] - Initial Release

### Added
- Base data analysis project template
- Automatic project structure generation
- Notebook workflow
- Modular Python source folders
- SQL folder structure
- Sample data generation

