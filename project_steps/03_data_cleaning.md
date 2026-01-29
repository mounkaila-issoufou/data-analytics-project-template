# Step 03 — Data Cleaning & Standardization

## Purpose of this step
This step transforms raw data into **clean, consistent, and technically reliable datasets**
that can be used safely for analytical modeling.

The objective is to fix **data quality issues identified during EDA**
while preserving the original business meaning of the data.

---

## Scope of data cleaning

Data cleaning focuses on:
- Structural consistency
- Data type correctness
- Handling missing or invalid values
- Basic business rule enforcement

This step does NOT include:
- Analytical aggregations
- KPI calculations
- Business-specific metrics
- Data modeling decisions

---

## Input data
- Source: `data/raw/`
- Data must reflect the original ingested datasets
- All transformations must be reproducible

---

## Output data
- Destination: `data/processed/`
- Format: analytics-friendly (e.g. Parquet)
- Cleaned datasets remain granular and close to the source

Example:

# Step 03 — Data Cleaning & Standardization

## Purpose of this step
This step transforms raw data into **clean, consistent, and technically reliable datasets**
that can be used safely for analytical modeling.

The objective is to fix **data quality issues identified during EDA**
while preserving the original business meaning of the data.

---

## Scope of data cleaning

Data cleaning focuses on:
- Structural consistency
- Data type correctness
- Handling missing or invalid values
- Basic business rule enforcement

This step does NOT include:
- Analytical aggregations
- KPI calculations
- Business-specific metrics
- Data modeling decisions

---

## Input data
- Source: `data/raw/`
- Data must reflect the original ingested datasets
- All transformations must be reproducible

---

## Output data
- Destination: `data/processed/`
- Format: analytics-friendly (e.g. Parquet)
- Cleaned datasets remain granular and close to the source

Example:

```text
data/processed/
├── orders_cleaned.parquet
├── customers_cleaned.parquet
├── products_cleaned.parquet
```


---

## Cleaning rules

### Column standardization
- Normalize column names (snake_case)
- Remove special characters
- Ensure consistent naming across datasets

---

### Data types
- Convert columns to appropriate data types
  - dates → date / timestamp
  - amounts → numeric
  - identifiers → string or integer
- Avoid implicit type inference downstream

---

### Missing values
- Identify mandatory vs optional fields
- Handle missing values explicitly:
  - imputation (if justified)
  - default values
  - or leave as null with documentation

All decisions must be documented.

---

### Duplicates
- Detect duplicate rows
- Apply deterministic deduplication rules
- Document deduplication logic

---

### Invalid values
- Remove or flag invalid records (e.g. negative amounts)
- Correct known formatting issues
- Preserve rows when business meaning is unclear

---

## Business rules (basic)
Only **simple and non-analytical** business rules are allowed, such as:
- Valid order statuses
- Non-negative monetary values
- Valid date ranges

Complex business logic belongs to the modeling step.

---

## Implementation guidelines

### Location of logic
All cleaning logic should be implemented in:
``src/cleaning/``


Notebooks should only:
- Call cleaning functions
- Orchestrate the workflow
- Validate outputs

---

### Notebook usage
Recommended notebook:

``notebooks/02_data_cleaning.ipynb``


Rules:
- Read from `data/raw/`
- Write only to `data/processed/`
- No hard-coded paths or values
- Clear markdown explanations

---

## Data quality validation
After cleaning:
- Row counts should be validated
- Mandatory fields should be checked
- Basic sanity checks should pass

These checks prepare the dataset for modeling.

---

## Documentation
All cleaning decisions must be documented:
- Why a rule was applied
- What data was affected
- Known limitations

This documentation ensures transparency and trust.

---

## Output of this step
At the end of this step:
- Cleaned datasets are available in `processed`
- Data is technically consistent
- Known issues are addressed or documented
- Data is ready for analytical modeling

This step bridges **raw data reality** and **analytics requirements**.
