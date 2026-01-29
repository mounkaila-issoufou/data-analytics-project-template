import sys
from pathlib import Path

PROJECT_STRUCTURE = [
    "data/raw",
    "data/processed",
    "data/curated",

    "notebooks",

    "src/ingestion",
    "src/cleaning",
    "src/modeling",
    "src/utils",

    "sql/ddl",
    "sql/dml",
    "sql/analytics",

    "dashboards",
    "docs",
]

README_LOCATIONS = [
    "",
    "data",
    "data/raw",
    "data/processed",
    "data/curated",
    "dashboards",
    "docs",
]

NOTEBOOKS = [
    "01_eda_raw_data.ipynb",
    "02_data_cleaning.ipynb",
    "03_data_modeling.ipynb",
    "04_business_analysis.ipynb",
]


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
    for file in [".gitignore", "requirements.txt"]:
        (base_path / file).touch(exist_ok=True)


# ---------- Sample data ----------
def generate_sample_data(base_path: Path):
    raw_path = base_path / "data/raw"

    customers = """customer_id,customer_name,segment
1,Alice,Consumer
2,Bob,Corporate
3,Charlie,SMB
"""

    products = """product_id,product_name,category
101,Laptop,Electronics
102,Headphones,Electronics
103,Desk,Furniture
"""

    regions = """region_id,region_name
10,Europe
11,North America
12,Asia
"""

    orders = """order_id,order_date,customer_id,product_id,region_id,status,amount
1001,2024-01-05,1,101,10,DELIVERED,1200.00
1002,2024-01-06,2,103,11,CANCELLED,450.00
1003,2024-01-07,1,102,10,SHIPPED,150.00
1004,2024-02-02,3,101,12,DELIVERED,1150.00
"""

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
