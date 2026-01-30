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