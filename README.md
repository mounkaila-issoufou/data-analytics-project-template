<!-- ========================= -->
<!-- PROJECT STATUS -->
<!-- ========================= -->

[![Version](https://img.shields.io/badge/Version-0.1.0-0066cc?style=flat-square)](#versioning)
[![Status](https://img.shields.io/badge/Status-Scaffolder-brightgreen?style=flat-square)](#project-status)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](#license)
![PyPI](https://img.shields.io/pypi/v/project-scaffolder)

---

<!-- ========================= -->
<!-- TECH STACK -->
<!-- ========================= -->

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776ab?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14%2B-336791?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Analytics-F2CC8F?style=flat-square&logo=powerbi&logoColor=black)](https://www.microsoft.com/power-platform/products/power-bi)

---

<!-- ========================= -->
<!-- ENGINEERING -->
<!-- ========================= -->

[![Tests](https://img.shields.io/badge/Tests-Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)](#testing)
[![CI](https://img.shields.io/badge/CI-GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)](#ci-cd)
[![Black](https://img.shields.io/badge/Code%20Style-Black-000000?style=flat-square&logo=python&logoColor=white)](https://black.readthedocs.io/)
[![Ruff](https://img.shields.io/badge/Linting-Ruff-46A2F1?style=flat-square)](https://docs.astral.sh/ruff/)
![Coverage](https://img.shields.io/badge/coverage-94%25-brightgreen)
[![Architecture](https://img.shields.io/badge/Architecture-Industrial_Grade-6A1B9A?style=flat-square)](#system-architecture)
[![Configuration](https://img.shields.io/badge/Config-Environment_Based-4CAF50?style=flat-square)](#configuration)

---

<!-- ========================= -->
<!-- DOMAIN -->
<!-- ========================= -->

[![Data Engineering](https://img.shields.io/badge/Data-Pipeline-ff6f00?style=flat-square)](#data-pipeline)


# Data Analytics Project Template

A professional, business-driven framework to structure end-to-end data analytics projects — from business framing to dashboard delivery.

It reflects how a **senior Data Analyst / Analytics Engineer** approaches a project:
starting from business questions, enforcing data governance, and delivering reliable insights.

---
## Why most analytics projects fail

- Start with notebooks, not business questions
- Mix exploration and production logic
- Lack reproducibility
- No documentation of KPIs
- Poor handover

This template solves these problems.


## Purpose of this repository

The goal of this template is to:

- Enforce **business-first thinking**
- Standardize **project structure and data layers**
- Improve **readability, scalability and maintainability**
- Avoid ad-hoc, notebook-only workflows
- Serve as a **reference framework** for professional data projects

This repository is **not a dataset** and **not a specific business case**.  
It is a **methodology and structure** that can be reused across projects.

---

## Project philosophy

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
├── Makefile
├── CONTRIBUTING.md
├── LICENSE
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
## ⚖️ Comparison with dbt-style workflows

| Aspect | This Template | dbt-style Workflow |
|--------|--------------|-------------------|
| Focus | End-to-end analytics lifecycle | Data transformation |
| Business framing | Explicit first step | Usually implicit |
| Raw / Processed / Curated separation | Enforced | Depends on modeling |
| KPI documentation | Built-in templates | External |
| Dashboard alignment | Explicit stage | Outside scope |

This template complements tools like dbt by structuring the entire analytics lifecycle,
not only the transformation layer.


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
project-scaffolder init my_project --package my_package
```

**With sample data:**
```bash
project-scaffolder init my_project --package my_package --with-sample-data
```

### 🛠 Alternative (without installation)

You can run the package directly as a module:

```bash
python -m project_scaffolder my_new_project
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for project history.


## 👤 Intended Audience

This template is designed for:

- Data Analysts

- Senior Data Analysts

- Analytics Engineers

- Professionals building structured analytics workflows

It is especially relevant for:

- Portfolio projects

- Take-home assignments

- Team standardization

- Analytics best-practice demonstrations


## 📌 Final note

This template reflects **how I approach data projects**:
with structure, clarity, and a strong focus on business value.

It is continuously evolving as practices improve and new lessons are learned.

## Contact & Link

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Mounkaila%20Issoufou-0077B5?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/abdoul-m-3a76b5214/)
[![GitHub](https://img.shields.io/badge/GitHub-mounkaila--issoufou-181717?style=flat-square&logo=github)](https://github.com/mounkaila-issoufou)
[![Email](https://img.shields.io/badge/Email-Contact%20Me-D14836?style=flat-square&logo=gmail)](mailto:mounkaila.issoufou025@gmail.com)


## 📜 License

MIT License – Free for educational & professional use