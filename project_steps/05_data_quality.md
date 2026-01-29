# Step 05 — Data Quality & Validation

## Purpose of this step
This step ensures that the analytical data model is **reliable, consistent, and trustworthy**
before it is used for analysis, SQL reporting, or dashboards.

The objective is to detect issues early, prevent silent errors,
and guarantee confidence in business metrics.

---

## Why data quality matters
Incorrect or inconsistent data leads to:
- Wrong KPIs
- Loss of trust from stakeholders
- Poor business decisions

This step acts as a **quality gate** between data modeling and data consumption.

---

## Scope of validation

Data quality checks apply to:
- Curated fact tables
- Curated dimension tables
- Relationships between facts and dimensions

This step does NOT introduce new transformations or metrics.

---

## Types of checks

### 1. Schema validation
- Expected columns exist
- Data types are correct
- No unexpected schema changes

---

### 2. Primary key checks
- Primary keys are unique
- No null values in primary keys

Examples:
- `order_id` in fact tables
- `customer_id` in dimension tables

---

### 3. Foreign key integrity
- All foreign keys in fact tables exist in dimensions
- No orphan records

Example:
- Every `customer_id` in `fact_orders` exists in `dim_customer`

---

### 4. Mandatory field checks
- Critical fields are not null
- Business-required attributes are present

Example:
- order_date
- order_status
- order_amount

---

### 5. Metric sanity checks
- No negative values where not allowed
- Totals are within expected ranges
- Sudden drops or spikes are flagged

---

### 6. Volume consistency
- Row counts are consistent with expectations
- No unexpected data loss between steps
- Trends align with historical patterns

---

## Implementation guidelines

### Location of logic
Data quality checks should be implemented in:
``src/utils/data_quality.py``


Checks should be:
- Modular
- Reusable
- Explicitly named

---

### Execution
Data quality checks can be:
- Run as part of notebooks
- Executed in scripts or pipelines
- Logged for traceability

Failures should:
- Raise clear errors
- Be easy to diagnose
- Block downstream steps if critical

---

## Reporting issues
When a data quality issue is detected:
- Describe the issue clearly
- Identify affected tables and columns
- Document potential business impact
- Decide whether to block or allow progression

All decisions should be documented.

---

## Documentation
Data quality rules and results should be:
- Described in project documentation
- Updated as business logic evolves
- Shared with stakeholders when relevant

---

## Output of this step
At the end of this step:
- Analytical tables pass quality checks
- Relationships are valid
- Metrics are trustworthy
- Data is ready for consumption

This step ensures **confidence in every number** produced downstream.
