from pathlib import Path
from project_scaffolder.config import INIT_PATHS

def create_init_files(base_path: Path):
    for location in INIT_PATHS:
        target_dir = base_path / location
        target_dir.mkdir(parents=True, exist_ok=True)
        (target_dir / "__init__.py").touch(exist_ok=True)