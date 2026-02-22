"""
Project configuration for project_scaffolder.
"""

# ============================================================
# PROJECT STRUCTURE (dynamic)
# ============================================================

def build_project_structure(package_name: str):
    return [
        # ---------- DATA ----------
        "data/raw",
        "data/processed",
        "data/curated",

        # ---------- NOTEBOOKS ----------
        "notebooks",

        # ---------- SOURCE CODE (dynamic package) ----------
        f"src/{package_name}",
        f"src/{package_name}/ingestion",
        f"src/{package_name}/cleaning",
        f"src/{package_name}/modeling",
        f"src/{package_name}/db",
        f"src/{package_name}/utils",

        # ---------- SQL ----------
        "sql/ddl",
        "sql/dml",
        "sql/analytics",

        # ---------- DASHBOARDS ----------
        "dashboards/powerbi",

        # ---------- DOCUMENTATION ----------
        "docs",

        # ---------- TESTS ----------
        "tests",
    ]


# ============================================================
# README LOCATIONS
# ============================================================

README_LOCATIONS = [
    "",
    "data",
    "data/raw",
    "data/processed",
    "data/curated",
    "notebooks",
    "dashboards",
    "docs",
    "sql",
    "src",
]


# ============================================================
# __init__.py PATHS (dynamic handling required in pipeline)
# ============================================================

def build_init_paths(package_name: str):
    return [
        f"src/{package_name}",
        f"src/{package_name}/ingestion",
        f"src/{package_name}/cleaning",
        f"src/{package_name}/modeling",
        f"src/{package_name}/db",
        f"src/{package_name}/utils",
    ]


INIT_PATHS = [
    "src",
    "src/ingestion",
    "src/cleaning",
    "src/modeling",
    "src/analytics",
    "src/viz",
    "src/utils",
]

# ============================================================
# NOTEBOOKS
# ============================================================

NOTEBOOKS = [
    "01_eda_raw_data.ipynb",
    "02_data_cleaning.ipynb",
    "03_data_modeling.ipynb",
    "04_business_analysis.ipynb",
    "05_dashboard.ipynb",
]


# ============================================================
# SAMPLE DATA (optional generation)
# ============================================================

CUSTOMERS_SAMPLE = """customer_id,customer_name,segment
1,Alice,Consumer
2,Bob,Corporate
3,Charlie,SMB
"""

PRODUCTS_SAMPLE = """product_id,product_name,category
101,Laptop,Electronics
102,Headphones,Electronics
103,Desk,Furniture
"""

REGIONS_SAMPLE = """region_id,region_name
10,Europe
11,North America
12,Asia
"""

ORDERS_SAMPLE = """order_id,order_date,customer_id,product_id,region_id,status,amount
1001,2024-01-05,1,101,10,DELIVERED,1200.00
1002,2024-01-06,2,103,11,CANCELLED,450.00
1003,2024-01-07,1,102,10,SHIPPED,150.00
1004,2024-02-02,3,101,12,DELIVERED,1150.00
"""