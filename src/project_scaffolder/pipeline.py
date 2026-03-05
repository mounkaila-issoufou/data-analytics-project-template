import sys
from pathlib import Path

from project_scaffolder.data.sample_data import generate_sample_data
from project_scaffolder.scaffold.directories import create_directories
from project_scaffolder.scaffold.files import create_root_files
from project_scaffolder.scaffold.init_files import create_init_files
from project_scaffolder.scaffold.logger import create_logger


def init_project(project_name: str, package_name: str, with_sample_data: bool):

    base_path = Path(project_name)

    if base_path.exists():
        print(f"❌ Project '{project_name}' already exists.")
        sys.exit(1)

    # Create base directory
    base_path.mkdir(parents=True, exist_ok=False)

    # Create full structure
    create_directories(base_path, package_name)

    # Create root-level files (README, pyproject, etc.)
    create_root_files(base_path, project_name, package_name)

    # Create logger config
    create_logger(base_path, package_name)

    # Create __init__.py files (dynamic package)
    create_init_files(base_path, package_name)

    # Optional sample data
    if with_sample_data:
        generate_sample_data(base_path, package_name)

    print(f"✅ Project '{project_name}' successfully initialized.")
