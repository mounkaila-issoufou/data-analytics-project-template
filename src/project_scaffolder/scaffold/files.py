from pathlib import Path
from project_scaffolder.config import README_LOCATIONS, NOTEBOOKS

def create_readmes(base_path: Path):
    for location in README_LOCATIONS:
        (base_path / location / "README.md").touch(exist_ok=True)


def create_notebooks(base_path: Path):
    notebooks_path = base_path / "notebooks"
    for nb in NOTEBOOKS:
        (notebooks_path / nb).touch(exist_ok=True)


def create_root_files(base_path: Path, package_name: str):
    gitignore = base_path / ".gitignore"
    gitignore.touch(exist_ok=True)

    with gitignore.open("a", encoding="utf-8") as f:
        f.write(
            "\n# Python\n"
            "__pycache__/\n"
            ".venv/\n"
            ".env\n"
            "*.pyc\n"
            ".ipynb_checkpoints/\n"
            "logs/\n"
        )

    (base_path / "requirements.txt").touch(exist_ok=True)
    (base_path / "pyproject.toml").touch(exist_ok=True)