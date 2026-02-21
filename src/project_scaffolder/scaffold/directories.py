from pathlib import Path
from project_scaffolder.config import PROJECT_STRUCTURE

def create_directories(base_path: Path):
    for folder in PROJECT_STRUCTURE:
        (base_path / folder).mkdir(parents=True, exist_ok=True)