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


def init_project(project_name: str, with_sample_data: bool):
    base_path = Path(project_name)

    if base_path.exists():
        print(f"❌ Project '{project_name}' already exists.")
        sys.exit(1)

    base_path.mkdir()

    create_directories(base_path)
    create_readmes(base_path)
    create_notebooks(base_path)
    create_root_files(base_path)
    create_logger(base_path)
    create_init_files(base_path)

    if with_sample_data:
        generate_sample_data(base_path)
        print("📦 Sample data generated in data/raw/")

    print(f"✅ Project '{project_name}' successfully initialized.")
