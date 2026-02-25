def build_project_readme(project_name: str, package_name: str) -> str:
    return rf"""# {project_name}

[![Version](https://img.shields.io/badge/Version-1.0-0066cc?style=flat-square)](#versioning)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776ab?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37726?style=flat-square&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14%2B-336791?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![PowerBI](https://img.shields.io/badge/Power%20BI-Analytics-F2CC8F?style=flat-square&logo=powerbi&logoColor=black)](https://www.microsoft.com/fr-fr/power-platform/products/power-bi)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](#licence)
[![Status](https://img.shields.io/badge/Status-Production-brightgreen?style=flat-square)](#)
    
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

## Stack Technologique

| Couche | Technologies |
|:---:|:---|
| **Ingestion & ETL** | [![Python](https://img.shields.io/badge/Python-Data%20Processing-3776ab?style=flat&logo=python&logoColor=white)](https://www.python.org/) [![Pandas](https://img.shields.io/badge/Pandas-Data%20Transformation-150458?style=flat&logo=pandas)](https://pandas.pydata.org/) |
| **Storage & Processing** | [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Data%20Warehouse-336791?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/) [![Parquet](https://img.shields.io/badge/Parquet-Columnar%20Format-2C3E50?style=flat)](https://parquet.apache.org/) |
| **Analysis & Exploration** | [![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37726?style=flat&logo=jupyter&logoColor=white)](https://jupyter.org/) [![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?style=flat&logo=numpy)](https://numpy.org/) |
| **Visualization & BI** | [![PowerBI](https://img.shields.io/badge/Power%20BI-Business%20Intelligence-F2CC8F?style=flat&logo=powerbi&logoColor=black)](https://www.microsoft.com/power-platform/products/power-bi) [![SQL](https://img.shields.io/badge/SQL-Analytics%20Queries-CC2927?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/) |
| **DevOps & Versioning** | [![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=flat&logo=git&logoColor=white)](https://git-scm.com/) [![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=flat&logo=github)](https://github.com/) |


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
- `src/{package_name}` → Python business logic  

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



## Installation

```text
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -e .

```
## Run pipeline

```text
python -m {package_name}.cli run 
```
or


```text
{package_name} run
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

"""