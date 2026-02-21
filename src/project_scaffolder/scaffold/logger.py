from pathlib import Path

def create_logger(base_path: Path):
    utils_path = base_path / "src" / "utils"
    utils_path.mkdir(parents=True, exist_ok=True)

    logger_file = utils_path / "logger.py"

    logger_file.write_text(
        """import logging
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
""",
        encoding="utf-8"
    )