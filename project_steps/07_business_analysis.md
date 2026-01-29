# Step 07 — Business Analysis & Insights

## Purpose of this step
This step focuses on interpreting analytical results
to produce **business insights, explanations, and recommendations**.

The objective is not to compute metrics,
but to **answer business questions and support decision-making**.

---

## Role of the data analyst at this stage

At this stage, the data analyst acts as:
- A translator between data and business
- A problem solver
- A decision support partner

The analyst does not just describe what happened,
but explains **why** and suggests **what to do next**.

---

## Inputs
- Analytics SQL queries
- KPI definitions
- Validated analytical data

No raw or processed data should be used directly.

---

## Analysis principles

Business analysis should:
- Be structured
- Be hypothesis-driven
- Focus on impact
- Avoid unnecessary technical details

---

## Typical analysis questions

Examples:
- How are orders evolving over time?
- Which products and regions drive performance?
- Where are cancellations concentrated?
- Are changes driven by volume, price, or mix?
- What explains month-over-month variations?

---

## Segmentation axes

Insights should be analyzed by:
- Time (day, week, month)
- Product / category
- Region
- Customer segment
- Order status

Segmentation helps identify patterns and root causes.

---

## KPI interpretation

For each KPI:
- Describe the trend
- Identify anomalies
- Explain possible drivers
- Quantify impact when possible

Avoid listing numbers without interpretation.

---

## Root cause analysis

When an issue is detected:
- Drill down by dimensions
- Compare with previous periods
- Isolate contributing factors
- Validate assumptions with data

Document findings clearly.

---

## Recommendations

Each major insight should lead to:
- A concrete recommendation
- A potential action
- A measurable expected impact

Examples:
- Improve logistics in high-cancellation regions
- Reassess pricing for underperforming products
- Target high-value customers with retention actions

---

## Notebook usage
Recommended notebook:

``notebooks/04_business_analysis.ipynb``


Rules:
- Clear narrative
- Charts support insights, not decoration
- Explicit assumptions and limitations

---

## Communication
Results should be:
- Understandable by non-technical stakeholders
- Structured logically
- Focused on business value

Use simple language and visuals.

---

## Documentation
Key insights and conclusions should be:
- Summarized in documentation
- Aligned with KPI definitions
- Reproducible

---

## Output of this step
At the end of this step:
- Business questions are answered
- Insights are clearly articulated
- Recommendations are actionable
- Data supports decision-making

This step is where **data creates value**.
