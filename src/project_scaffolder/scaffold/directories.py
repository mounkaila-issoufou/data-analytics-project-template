from pathlib import Path

from project_scaffolder.config import build_project_structure


def create_directories(base_path: Path, package_name: str):
    structure = build_project_structure(package_name)

    for folder in structure:
        (base_path / folder).mkdir(parents=True, exist_ok=True)
