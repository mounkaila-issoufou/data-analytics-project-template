def build_project_precommit(project_name: str, package_name: str) -> str:
    return rf"""# {project_name}
repos:
  - repo: https://github.com/psf/black
    rev: 24.0
    hooks:
      - id: black

  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.0.326
    hooks:
      - id: ruff
    """