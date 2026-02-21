from pathlib import Path
import sys

from project_scaffolder.scaffold.directories import create_directories
from project_scaffolder.scaffold.files import create_root_files
from project_scaffolder.scaffold.init_files import create_init_files
from project_scaffolder.scaffold.logger import create_logger
from project_scaffolder.data.sample_data import generate_sample_data


def init_project(project_name: str, with_sample_data: bool):

    base_path = Path(project_name)

    if base_path.exists():
        print(f"❌ Project '{project_name}' already exists.")
        sys.exit(1)

    base_path.mkdir()

    create_directories(base_path)
    create_root_files(base_path)
    create_logger(base_path)
    create_init_files(base_path)

    if with_sample_data:
        generate_sample_data(base_path)

    print(f"✅ Project '{project_name}' successfully initialized.")