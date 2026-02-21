# Data Analytics Project Template

This repository provides a **standardized, reusable and business-driven template**
to structure data analytics projects, from initial business framing to final dashboards.

It reflects how a **senior Data Analyst / Analytics Engineer** approaches a project:
starting from business questions, enforcing data governance, and delivering reliable insights.

---

## 🎯 Purpose of this repository

The goal of this template is to:

- Enforce **business-first thinking**
- Standardize **project structure and data layers**
- Improve **readability, scalability and maintainability**
- Avoid ad-hoc, notebook-only workflows
- Serve as a **reference framework** for professional data projects

This repository is **not a dataset** and **not a specific business case**.  
It is a **methodology and structure** that can be reused across projects.

---

## 🧠 Project philosophy

A data project should answer business questions **before** manipulating data.

This template follows these principles:
- Clear separation of concerns
- Explicit documentation of assumptions
- Strong data governance (raw / processed / curated)
- Analytics-ready data modeling
- Reproducible and explainable workflows

---

## 🔄 Standard project lifecycle

Each project built with this template follows the steps below:

### 0️⃣ Business framing
- Define business questions
- Identify KPIs
- Clarify scope, assumptions and limits

### 1️⃣ Data ingestion
- Load raw data
- Preserve source format
- Document origin and extraction logic

### 2️⃣ Data exploration (EDA)
- Understand distributions and anomalies
- Identify data quality issues
- Validate business logic

### 3️⃣ Data cleaning
- Standardize columns and data types
- Handle missing values
- Apply basic business rules

### 4️⃣ Data modeling
- Define analytical grain
- Build fact and dimension tables
- Create analytics-ready datasets

### 5️⃣ Data quality checks
- Validate keys and relationships
- Detect inconsistencies
- Ensure trust in outputs

### 6️⃣ Analytics SQL layer
- Expose curated data via SQL
- Build reusable analytical queries
- Define KPIs consistently

### 7️⃣ Business analysis
- Answer business questions
- Perform trend and diagnostic analysis
- Avoid data transformations at this stage

### 8️⃣ Dashboarding
- Design decision-oriented dashboards
- Focus on clarity and actionability
- Align visuals with KPIs

### 9️⃣ Documentation & handover
- Document data models and KPIs
- Capture assumptions and limitations
- Ensure project continuity

---
```text
.
├── project_steps/            # Business & methodological documentation
├── templates/                # Markdown templates (KPIs, data dictionary, etc.)
├── example_structure/        # Example generated project tree
├── docs/                     # Architecture & design decisions
│
├── src/
│   └── project_scaffolder/   # Main Python package
│       ├── __init__.py
│       ├── cli.py
│       ├── pipeline.py
│       ├── config.py
│       ├── scaffold/
│       ├── data/
│       └── utils/
│
├── tests/                    # Unit tests
│
├── pyproject.toml            # Packaging configuration
├── .gitignore
└── README.md
```

Each folder exists for a reason and reflects a specific responsibility in the project lifecycle.

---

## ⚙️ Project generator

This repository includes a Python script that automatically generates
a **standard data analytics project structure** based on this template.

The goal is to:
- Save time
- Enforce best practices
- Ensure consistency across projects

---

## 👤 Intended audience

This template is designed for:
- Data Analysts
- Senior Data Analysts
- Analytics Engineers
- Anyone building analytics projects in a professional environment

It is especially relevant for:
- Portfolio projects
- Take-home assignments
- Team standardization
- Analytics best-practice demonstrations

---

## 🚀 How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/---/project-scaffolder.git
cd project-scaffolder
```
### 2️⃣ Create a virtual environment
```bash
python -m venv .venv
```

Activate it:

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**
```bash
.venv\Scripts\activate
```

### 3️⃣ Install the package in editable mode
```bash
pip install -e .
```

### 4️⃣ Run the CLI

**Create a new project:**
```bash
project-scaffolder my_new_project
```

**With sample data:**
```bash
project-scaffolder my_new_project --with-sample-data
```

### 🛠 Alternative (without installation)

You can run the package directly as a module:

```bash
python -m project_scaffolder my_new_project
```
## 📌 Final note

This template reflects **how I approach data projects**:
with structure, clarity, and a strong focus on business value.

It is continuously evolving as practices improve and new lessons are learned.
