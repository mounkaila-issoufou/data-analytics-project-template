# industrial-digital-twin

<!-- ========================= -->
<!-- PROJECT STATUS -->
<!-- ========================= -->

[![Version](https://img.shields.io/badge/Version-1.2-0066cc?style=flat-square)](#versioning)
[![Status](https://img.shields.io/badge/Status-Production-brightgreen?style=flat-square)](#project-status)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](#license)

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
[![Architecture](https://img.shields.io/badge/Architecture-Industrial_Grade-6A1B9A?style=flat-square)](#system-architecture)
[![Configuration](https://img.shields.io/badge/Config-Environment_Based-4CAF50?style=flat-square)](#configuration)

---

<!-- ========================= -->
<!-- DOMAIN -->
<!-- ========================= -->

[![Data Engineering](https://img.shields.io/badge/Data-Pipeline-ff6f00?style=flat-square)](#data-pipeline)
[![Analytics](https://img.shields.io/badge/Analytics-OEE%20%26%20Downtime-1E88E5?style=flat-square)](#analytics)
    
## 🎯 Project Overview

Short description of the business problem.


## 📚 Table des matières
- [Objectif du projet](#objectif-du-projet)
- [Contexte industriel](#contexte-industriel)
- [Source et nature des données](#source-et-nature-des-données)
- [Principe de mesure de la non-production](#principe-de-mesure-de-la-non-production)
- [Périmètre d’analyse](#périmètre-danalyse)
- [Démarche analytique](#démarche-analytique)
- [Approche données](#approche-données)
- [Couche analytique (Data Warehouse)](#couche-analytique-data-warehouse)
- [Architecture globale](#architecture-globale)
- [Stack technologique](#stack-technologique)
- [KPIs industriels clés](#kpis-industriels-clés)
- [Organisation du repository](#organisation-du-repository)
- [Dashboards Power BI](#dashboards-power-bi)
- [Pipeline](#le-pipeline)
- [Installation](#installation)
- [Organisation du projet](#structure-du-projet)
- [Documentation](#documentation-détaillée)

---

## 🧠 Business Context

- Stakeholders:
- Business Objective:
- Key Decisions to Support:

---

## 🏗 System Architecture

```mermaid
flowchart LR

    subgraph Sources
        A[Shopfloor Systems]
        B[IoT Sensors]
        C[ERP / MES]
    end

    subgraph Bronze Layer - Raw Data
        D[Raw Data Lake]
    end

    subgraph Silver Layer - Cleaned and Transformed
        E[Data Cleaning]
        F[Data Transformation]
    end

    subgraph Gold Layer - Business Ready
        G[Data Warehouse]
        H[SQL KPIs]
    end

    subgraph Consumption
        I[BI Dashboards]
        J[Operational Decisions]
    end

    A --> D
    B --> D
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I
    I --> J
```
## ⚙️ Technology Stack

| Layer | Tools |
|:---|:---|
| Ingestion & ETL | Python, Pandas |
| Storage & Processing | PostgreSQL, Parquet |
| Analysis & Exploration | Jupyter, NumPy |
| Visualization & BI | Power BI, SQL |
| DevOps & Versioning | Git, GitHub, GitHub Actions |

---

## 📊 Key KPIs

| KPI | Business Definition | Technical Definition |
|-----|---------------------|----------------------|
|     |                     |                      |

---

## 🗂 Data Sources

| Source | Description | Owner |
|--------|------------|-------|
|        |            |       |

---

## 🏗 Project Structure

This project follows a standardized data analytics structure:

- `data/raw` → raw source data  
- `data/processed` → cleaned & transformed data  
- `data/curated` → analytics-ready datasets  
- `sql/` → SQL logic for modeling and analytics  
- `notebooks/` → exploration & analysis  
- `src/digital_twin` → Python business logic  

---

## 🔄 Analytical Workflow

1. Business framing  
2. Data ingestion  
3. Data cleaning  
4. Data modeling  
5. KPI validation  
6. Business analysis  
7. Dashboarding  

---

## ⚠ Assumptions & Limitations

-  

---

## 🚀 Next Steps

-  
## Dashboards Power BI

Les dashboards Power BI sont conçus pour offrir une **lecture claire, synthétique et orientée décision** des performances commerciales.

### Emplacement des fichiers

```text
dashboards/
└── powerbi/
    ├── sales_performance.pbix
    └── screenshots/
```

## Le pipeline

initialise les tables SQL,

charge le staging,

alimente les dimensions,

peuple la table de faits.



## 🚀 Installation
## Installation

### 1️⃣ Clone the repository

```bash
git clone git@github.com:mounkaila-issoufou/industrial-downtime-analytics.gitcd industrial-downtime-analytics
```
### 2️⃣ Create a virtual environment

```bash
```text
python -m venv .venv
```
Activate the environment:

**Windows**

```bash
.\.venv\Scripts\activate
```
**macOS / Linux**

```bash
source .venv/bin/activate
```
### 3️⃣ Install the project (editable mode)

```bash
python -m pip install --upgrade pip
python -m pip install -e .
```
Editable mode (-e) allows local development and CLI usage.

### 🔄 Regenerate dependencies (after updating pyproject.toml)

If you add or modify dependencies in `pyproject.toml`, regenerate the locked `requirements.txt` file with:

```bash
pip install pip-tools
pip-compile pyproject.toml -o requirements.txt
```

This will:

- Resolve all transitive dependencies

- Lock exact versions

- Keep requirements.txt fully synchronized with pyproject.toml

⚠️ Do not edit requirements.txt manually — it is automatically generated.


### 🧱 Database Initialization

Before running the pipeline for the first time:

```bash
digital_twin init
```
This command:

- Creates schemas (stg, ops, dw)

- Creates all staging, operational, and data warehouse tables
## Run pipeline

- Prepares the full database structure

### 🔄 Optional – Reset Data

To truncate all data (without dropping tables):
```bash
digital_twin reset
```
This clears all data layers while keeping the database structure intact.

### ▶ Run the Data Pipeline

To execute the full end-to-end pipeline:
```bash
digital_twin run
```
or

```bash
python -m digital_twin.cli run
```
- The pipeline performs:

- Mock industrial data generation

- Staging layer load

- Operational layer transformation

- Data warehouse population

### 🔁 Full Refresh (Reset + Run)

For a complete refresh:

```bash
digital_twin full-refresh
```
## 🏗 Execution Flow Overview

```bash
init         → Create schemas & tables
reset        → Truncate data layers
run          → Execute full DML pipeline
full-refresh → Reset + Run
```

### 🧹 Pre-commit hooks (Automatic code checks)

We use `pre-commit` to ensure code quality and consistent formatting before committing. It automatically runs tools like **black** (code formatter) and **ruff** (linter) on your modified files.

#### 1️⃣ Install pre-commit

```bash
pip install pre-commit
```
#### 2️⃣ Add the configuration file

Create a ``.pre-commit-config.yaml`` at the root of your project:

```bash
repos:
  - repo: https://github.com/psf/black
    rev: 24.0
    hooks:
      - id: black

  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.0.326
    hooks:
      - id: ruff
```
#### 3️⃣ Activate pre-commit hooks

```bash
pre-commit install
```

This installs the Git hook. From now on, every git commit will automatically check your code.

#### 4️⃣ Usage

Simply work as usual and commit your changes:

```bash
git add .
git commit -m "feat: add new feature"
```

Pre-commit will check and format modified files automatically.

If issues are found, fix them and commit again.

### 5️⃣ Optional: run on all files

To apply hooks to all files in the project (useful when first setting up):

```bash
pre-commit run --all-files

```

## Résultats attendus



---

## Documentation détaillée

La documentation fonctionnelle et technique du projet est centralisée dans le dossier `docs/` :

- **Architecture globale**  
  👉 [`docs/architecture_overview.md`](docs/architecture_overview.md)

- **Modèle de données (Star Schema)**  
  👉 [`docs/data_model.md`](docs/data_model.md)

- **Dictionnaire de données**  
  👉 [`docs/data_dictionary.md`](docs/data_dictionary.md)

- **Définition des KPI métier**  
  👉 [`docs/kpi_definitions.md`](docs/kpi_definitions.md)

- **Hypothèses, périmètre et limites du projet**  
  👉 [`docs/assumptions_and_limits.md`](docs/assumptions_and_limits.md)


## ⚠️ Limites


---

## 👤 Auteur
Projet de portfolio **Data Analyst senior** – Abdoul Mounkaila Issoufou

## Contact & Liens

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Mounkaila%20Issoufou-0077B5?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/abdoul-m-3a76b5214/)
[![GitHub](https://img.shields.io/badge/GitHub-mounkaila--issoufou-181717?style=flat-square&logo=github)](https://github.com/mounkaila-issoufou)
[![Email](https://img.shields.io/badge/Email-Contact%20Me-D14836?style=flat-square&logo=gmail)](mailto:mounkaila.issoufou025@gmail.com)


## Licence

Ce projet est sous licence **MIT** – libre d’utilisation à des fins éducatives et professionnelles.

