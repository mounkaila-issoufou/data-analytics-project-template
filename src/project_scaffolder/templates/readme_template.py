def build_project_readme(project_name: str, package_name: str) -> str:
    return f"""# {project_name}

## 🎯 Project Overview

Short description of the business problem.

---

## 🧠 Business Context

- Stakeholders:
- Business Objective:
- Key Decisions to Support:

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
"""