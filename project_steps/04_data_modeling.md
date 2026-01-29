# Step 04 — Data Modeling (Analytical Modeling)

## Purpose of this step
This step transforms cleaned datasets into an **analytics-ready data model**
designed to answer business questions efficiently and consistently.

The objective is to create a **clear, scalable, and performant analytical layer**
that can be used by SQL, BI tools, and downstream analyses.

---

## Modeling philosophy

The analytical model is:
- Business-oriented
- Read-optimized
- Explicitly structured
- Stable over time

This step prioritizes:
- Simplicity over normalization
- Clarity over flexibility
- Consistency over convenience

---

## Input data
- Source: `data/processed/`
- Data is clean, typed, and standardized
- No raw data is used at this stage

---

## Output data
- Destination: `data/curated/`
- Format: columnar analytics format (e.g. Parquet)
- Tables are final and ready for consumption

Example:

```text
data/curated/
├── fact_orders.parquet
├── dim_customer.parquet
├── dim_product.parquet
├── dim_region.parquet
├── dim_date.parquet

```


---

## Grain definition

The grain of the fact table must be explicitly defined and documented.

Example:
- **1 row = 1 order**

All metrics and analyses must be valid at this grain.
If a question cannot be answered at this level, the grain must be reconsidered.

---

## Fact tables

Fact tables:
- Represent business events
- Contain quantitative measures
- Reference dimensions via foreign keys

Example measures:
- order_amount
- order_count (implicit)
- cancellation_flag

Fact tables must:
- Be narrow
- Avoid descriptive attributes
- Avoid derived KPIs

---

## Dimension tables

Dimension tables:
- Provide descriptive context
- Contain stable attributes
- Enable slicing and filtering

Examples:
- customer
- product
- region
- date

Dimensions should:
- Use surrogate keys when appropriate
- Be consistent across facts
- Support slowly changing attributes if needed

---

## Date dimension
A dedicated date dimension is mandatory.

Typical attributes:
- full_date
- year
- quarter
- month
- week
- day
- weekday_flag

This ensures consistent temporal analysis across all metrics.

---

## Modeling patterns

Recommended pattern:
- Star schema

Benefits:
- Simpler queries
- Better BI tool compatibility
- Improved performance
- Clear mental model for analysts

Snowflake schemas should only be used when justified.

---

## Implementation guidelines

### Location of logic
All modeling logic should be implemented in:

``src/modeling/``


Typical responsibilities:
- Build fact tables
- Build dimension tables
- Enforce keys and relationships
- Apply final business rules

---

### Notebook usage
Recommended notebook:

``notebooks/03_data_modeling.ipynb``


Rules:
- Read only from `data/processed/`
- Write only to `data/curated/`
- No exploratory logic
- Clear explanation of modeling decisions

---

## Validation checks
Before publishing curated tables:
- Validate row counts
- Validate foreign key integrity
- Validate metric consistency
- Validate grain assumptions

---

## Documentation
All modeling decisions must be documented:
- Fact grain
- Dimension definitions
- Key design choices
- Known limitations

This documentation ensures trust and long-term maintainability.

---

## Output of this step
At the end of this step:
- Curated analytical tables are available
- Data is ready for SQL, BI, and analysis
- Business questions defined in Step 00 can be answered
- The analytics layer is stable and reusable

This step is the **core of the analytics value chain**.

