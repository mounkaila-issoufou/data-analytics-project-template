from pathlib import Path

from project_scaffolder.config import (
    CUSTOMERS_SAMPLE,
    ORDERS_SAMPLE,
    PRODUCTS_SAMPLE,
    REGIONS_SAMPLE,
)


def generate_sample_data(base_path: Path, package_name: str):
    raw_path = base_path / "data/raw"
    raw_path.mkdir(parents=True, exist_ok=True)

    (raw_path / "customers.csv").write_text(CUSTOMERS_SAMPLE)
    (raw_path / "products.csv").write_text(PRODUCTS_SAMPLE)
    (raw_path / "regions.csv").write_text(REGIONS_SAMPLE)
    (raw_path / "orders.csv").write_text(ORDERS_SAMPLE)
