# Step 01 — Data Ingestion & Raw Data Governance

## Purpose of this step
This step defines how data is **ingested, stored, and governed** in its raw form.

The objective is to ensure:
- Traceability of data sources
- Reproducibility of the pipeline
- Clear separation between raw and transformed data

At this stage, **no data transformation is allowed**.

---

## Definition of raw data
Raw data represents the **original state of the data** as received from the source system.

Raw data must:
- Preserve the original format
- Remain immutable
- Be reproducible from the source
- Serve as a reference point for audits and debugging

---

## Data sources
For each dataset, the following information must be documented:

- Source system (e.g. CRM, ERP, API, CSV export)
- Extraction method
- Extraction date
- Data owner (if applicable)
- Original format (CSV, JSON, etc.)

This information should be recorded in the raw data README.

---

## Raw data storage rules

### Directory
```data/raw/```


### Rules
- Raw files must never be modified once ingested
- No cleaning, filtering, or enrichment is allowed
- Column names and data types must remain unchanged
- Multiple extractions should be versioned or timestamped

---

## File naming conventions
Raw data files should follow a clear and consistent naming pattern.

Example:
```orders_2024_01_15.csv```
```customers_2024_01_15.csv```
```products_2024_01_15.csv```


This ensures traceability and reproducibility.

---

## Raw data documentation

Each raw data folder must include a `README.md` describing:

- Dataset description
- Source system
- Extraction logic
- Known data issues
- Expected schema (if available)

This documentation is mandatory and should be updated when new datasets are added.

---

## Ingestion logic

Data ingestion logic should be implemented in:

```src/ingestion/```


Responsibilities of ingestion scripts:
- Load data from the source
- Save data into `data/raw/`
- Apply minimal validation (file existence, format, basic schema check)
- Log ingestion metadata if needed

No business logic or transformations should be included.

---

## Validation at ingestion stage
Allowed validations:
- File existence
- File readability
- Basic schema presence (columns exist)

Not allowed:
- Removing rows
- Changing values
- Applying business rules

---

## Assumptions
- Source data is considered the single source of truth
- Ingestion failures must be explicit and logged
- Raw data reflects the state of the source at extraction time

---

## Output of this step
At the end of this step:
- Raw data is safely stored and documented
- Ingestion logic is reproducible
- No transformations have been applied
- Downstream steps can rely on raw data integrity

This step establishes **trust in the data pipeline**.
