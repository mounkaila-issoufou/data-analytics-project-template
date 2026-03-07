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
- Modular project scaffolder architecture (`project_scaffolder`)
- Template system for project file generation
- Pre-commit configuration template
- Docker compose template
- Changelog template
- SQL project structure (`analytics`, `ddl`, `dml`, `reset`)
- Logging utility for generated projects
- Automatic test suite for the scaffolder
- CI pipeline for automated testing
- Test coverage reporting (94%)

### Changed
- Refactored scaffolding architecture
- Improved configuration management
- Improved README project template
- Improved root file generation logic
- Improved code formatting and linting workflow

### Generated Project Improvements
Generated projects now include:

- Structured data directories (`raw`, `processed`, `curated`)
- Modular Python source structure
- SQL project structure
- Notebook workflow
- Dashboard directories (PowerBI / Looker)
- Tests directory
- Logs directory
- Pre-configured project documentation

---

## [0.1.0] - Initial Release

### Added
- Base data analysis project template
- Automatic project structure generation
- Notebook workflow
- Modular Python source folders
- SQL folder structure
- Sample data generation