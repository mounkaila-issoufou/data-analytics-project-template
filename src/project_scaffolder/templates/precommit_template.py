def build_project_precommit(project_name: str, package_name: str) -> str:
    return r"""
default_language_version:
  python: python3

repos:
  - repo: https://github.com/psf/black
    rev: 24.4.2
    hooks:
      - id: black
        language: system

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.5.0
    hooks:
      - id: ruff
        args: [--fix]
        language: system
      - id: ruff-format
        language: system

  - repo: local
    hooks:
      - id: pytest
        name: pytest
        entry: pytest
        language: system
        pass_filenames: false
        stages: [pre-push]

    """
