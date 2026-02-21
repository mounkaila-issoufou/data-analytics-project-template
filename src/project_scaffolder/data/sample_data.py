from pathlib import Path
from project_scaffolder.config import customers, products, regions, orders

def generate_sample_data(base_path: Path):
    raw_path = base_path / "data/raw"
    raw_path.mkdir(parents=True, exist_ok=True)

    (raw_path / "customers.csv").write_text(customers)
    (raw_path / "products.csv").write_text(products)
    (raw_path / "regions.csv").write_text(regions)
    (raw_path / "orders.csv").write_text(orders)