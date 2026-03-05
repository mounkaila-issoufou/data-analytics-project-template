from pathlib import Path

from project_scaffolder.config import build_init_paths


def create_init_files(base_path: Path, package_name: str):
    init_paths = build_init_paths(package_name)
    for location in init_paths:
        target_dir = base_path / location
        target_dir.mkdir(parents=True, exist_ok=True)
        (target_dir / "__init__.py").touch(exist_ok=True)
