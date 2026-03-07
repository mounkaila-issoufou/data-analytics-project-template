import sys
from pathlib import Path

from .data.sample_data import generate_sample_data
from .scaffold.directories import create_directories
from .scaffold.files import (
    create_notebooks,
    create_readmes,
    create_root_files,
)
from .scaffold.init_files import create_init_files
from .scaffold.logger import create_logger


def init_project(
    project_name: str,
    package_name: str,
    base_path: str | Path = ".",
    with_sample_data: bool = False,
):
    base_path = Path(base_path)
    project_path = base_path / project_name

    if project_path.exists():
        print(f"❌ Project '{project_name}' already exists.")
        sys.exit(1)

    project_path.mkdir(parents=True)

    create_directories(project_path, package_name)

    create_readmes(project_path)
    create_notebooks(project_path)

    # ✅ CORRECTION ICI
    create_root_files(project_path, project_name, package_name)

    create_logger(project_path, package_name)
    create_init_files(project_path, package_name)

    if with_sample_data:
        generate_sample_data(project_path)
        print("📦 Sample data generated in data/raw/")

    print(f"✅ Project '{project_name}' successfully initialized.")

    return project_path
