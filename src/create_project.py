import sys
from pathlib import Path
from src.config import PROJECT_STRUCTURE, README_LOCATIONS, NOTEBOOKS
from src.config import customers, products, regions, orders

# ---------- Core structure ----------
def create_directories(base_path: Path):
    for folder in PROJECT_STRUCTURE:
        (base_path / folder).mkdir(parents=True, exist_ok=True)


def create_readmes(base_path: Path):
    for location in README_LOCATIONS:
        (base_path / location / "README.md").touch(exist_ok=True)


def create_notebooks(base_path: Path):
    notebooks_path = base_path / "notebooks"
    for nb in NOTEBOOKS:
        (notebooks_path / nb).touch(exist_ok=True)


def create_root_files(base_path: Path):
    gitignore = base_path / ".gitignore"
    gitignore.touch(exist_ok=True)

    with gitignore.open("a", encoding="utf-8") as f:
        f.write("\n# Python\n")
        f.write("__pycache__/\n")
        f.write(".venv/\n")
        f.write(".env\n")
        f.write("*.pyc\n")
        f.write("__pycache__/\n")
        f.write(".ipynb_checkpoints/\n")
        f.write("logs/\n")

    (base_path / "requirements.txt").touch(exist_ok=True)


def create_logger(base_path: Path):
    utils_path = base_path / "src" / "utils"
    utils_path.mkdir(parents=True, exist_ok=True)

    logger_file = utils_path / "logger.py"

    logger_code = """import logging
from pathlib import Path


def setup_logger(
    name: str = "edtech_pipeline",
    log_file: str = "pipeline.log",
    level: int = logging.INFO
) -> logging.Logger:

    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(log_dir / log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
"""

    logger_file.write_text(logger_code, encoding="utf-8")

def create_init_files(base_path: Path):
    init_paths = [
        base_path / "src",
        base_path / "src" / "utils",
        base_path / "src" / "ingestion",
        base_path / "src" / "cleaning",
        base_path / "src" / "modeling",
    ]

    for path in init_paths:
        (path / "__init__.py").touch(exist_ok=True)

def create_run_pipeline(base_path: Path):
    run_file = base_path / "run_pipeline.py"

    run_code = """from src.utils.logger import setup_logger

logger = setup_logger()


def main():
    logger.info("🚀 Pipeline started")

    # TODO: ingestion
    # TODO: cleaning
    # TODO: modeling

    logger.info("✅ Pipeline finished successfully")


if __name__ == "__main__":
    main()
"""

    run_file.write_text(run_code, encoding="utf-8")




# ---------- Sample data ----------
def generate_sample_data(base_path: Path):
    raw_path = base_path / "data/raw"



    (raw_path / "customers.csv").write_text(customers)
    (raw_path / "products.csv").write_text(products)
    (raw_path / "regions.csv").write_text(regions)
    (raw_path / "orders.csv").write_text(orders)


# ---------- Init ----------
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
    create_run_pipeline(base_path)
    
    if with_sample_data:
        generate_sample_data(base_path)
        print("📦 Sample data generated in data/raw/")

    print(f"✅ Project '{project_name}' successfully initialized.")


# ---------- CLI ----------
if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        print("Usage: python init_project.py <project_name> [--with-sample-data]")
        sys.exit(1)

    project_name = sys.argv[1]
    with_sample_data = "--with-sample-data" in sys.argv

    init_project(project_name, with_sample_data)
