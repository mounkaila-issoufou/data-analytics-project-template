# Step 06 — SQL Layer (DDL, DML & Analytics)

## Purpose of this step
This step defines how analytical data structures are created, populated,
and queried using SQL.

The objective is to:
- Separate responsibilities clearly
- Ensure maintainability
- Guarantee metric consistency
- Support BI and analytics consumption

---

## SQL layer responsibilities

The SQL layer is divided into three distinct components:

### 1. DDL — Data Definition Language
Defines schemas and table structures.

### 2. DML — Data Manipulation Language
Populates and maintains analytical tables.

### 3. Analytics SQL
Exposes KPIs and business queries.

Each layer has a clear and non-overlapping role.

---

## Directory structure

```text
sql/
├── ddl/
├── dml/
└── analytics/
```


---

## DDL layer
Responsibilities:
- Create schemas
- Create fact and dimension tables
- Define constraints where applicable

Rules:
- No data manipulation
- Idempotent scripts
- Fully version-controlled

---

## DML layer
Responsibilities:
- Load data into dimensions and facts
- Apply final transformations
- Handle incremental loads
- Apply data corrections when necessary

Examples:
- INSERT INTO dim_customer
- MERGE INTO fact_orders
- UPDATE for business rule corrections

Rules:
- No table creation
- Clear separation between full and incremental loads
- Explicit filters and joins

---

## Analytics SQL layer
Responsibilities:
- Define KPIs
- Answer business questions
- Support dashboards and reporting

Rules:
- Read-only queries
- No data modification
- Business logic clearly documented

---

## Data sources
- DML reads from: `data/curated/` or staging tables
- Analytics reads from: final analytical tables only

---

## KPI governance
- KPIs are defined once
- SQL logic is the source of truth
- Any KPI change must go through DML or modeling layers

---

## Validation
- DML outputs must match curated data expectations
- Row counts and totals must be validated
- Analytics results must be reproducible

---

## Output of this step
At the end of this step:
- Tables are created (DDL)
- Data is loaded and maintained (DML)
- KPIs are exposed and queryable (Analytics)

This step establishes a **robust and professional SQL architecture**.
