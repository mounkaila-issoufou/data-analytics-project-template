# Step 02 — Data Exploration (EDA)

## Purpose of this step
The goal of this step is to **understand the raw data** before applying any transformation.

Exploratory Data Analysis (EDA) is used to:
- Assess data structure and completeness
- Identify anomalies and inconsistencies
- Validate business assumptions
- Inform cleaning and modeling decisions

No data is modified or persisted during this step.

---

## Principles of data exploration

EDA is:
- Read-only
- Investigative
- Documented

EDA is NOT:
- Data cleaning
- Feature engineering
- Business analysis
- Data modeling

This strict separation ensures clarity and reproducibility.

---

## Data sources used
- Data must be read exclusively from:

data/raw/


No processed or curated data should be used at this stage.

---

## Typical analyses performed

### Structure & schema
- Number of rows and columns
- Column names and data types
- Identification of candidate keys
- Presence of duplicates

---

### Completeness
- Missing values per column
- Patterns of missingness
- Mandatory vs optional fields

---

### Distributions
- Numerical distributions (min, max, percentiles)
- Categorical value counts
- Outliers and extreme values

---

### Temporal checks
- Date ranges
- Missing or duplicated dates
- Unexpected gaps or spikes

---

### Business logic validation
- Invalid statuses
- Negative or zero monetary values
- Unexpected combinations (e.g. cancelled but delivered)

Any inconsistency should be noted, not fixed.

---

## Documentation of findings

All observations must be documented:
- Either directly in the notebook
- Or summarized in a markdown file if needed

Examples:
- Known data quality issues
- Suspected data collection problems
- Columns requiring special cleaning logic
- Assumptions that need confirmation

These findings directly inform Step 03 (Data Cleaning).

---

## Notebook usage

Recommended location:

notebooks/01_eda_raw_data.ipynb


Notebook rules:
- No writes to disk
- No overwriting of raw data
- Clear markdown explanations
- Reproducible execution

---

## Output of this step
At the end of this step:
- Data structure is fully understood
- Data quality issues are identified
- Cleaning and modeling strategies are informed
- No data has been altered

EDA provides the **foundation for all downstream decisions**.

---

## Common pitfalls to avoid
- Applying fixes during exploration
- Mixing EDA with business analysis
- Creating derived metrics too early
- Ignoring documented anomalies

This step exists to observe, not to act.
