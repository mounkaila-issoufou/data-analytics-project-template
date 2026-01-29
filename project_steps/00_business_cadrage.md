# Step 00 — Business Framing & Project Scope

## Purpose of this step
This step defines the **business context**, **objectives**, and **key questions**
that the data project aims to address.

No data is explored or transformed at this stage.
The goal is to ensure that all downstream technical work serves a clear business purpose.

---

## Business context
[Describe the business domain briefly: e.g. e-commerce, SaaS, marketplace, operations, etc.]

Example:
This project focuses on analyzing customer orders to understand sales performance,
customer behavior, and operational issues such as cancellations.

---

## Main business problem
What is the core problem this project is trying to solve?

Example:
How do orders evolve over time in terms of volume and value, and what factors explain
order cancellations across products, regions, and customers?

---

## Business questions

### Orders & volume
- How many orders are placed, delivered, shipped, or cancelled?
- How does the number of orders evolve over time?
- How do current-period orders compare to the previous month?

---

### Financial performance
- What is the total order amount for delivered, shipped, and cancelled orders?
- How does revenue evolve month-over-month?
- Which products and regions generate the highest order value?

---

### Products
- Which products are ordered the most?
- How do orders distribute across product categories?
- How does product performance evolve over time?

---

### Customers
- How many active customers are there?
- How many orders does each customer place?
- Which customers generate the most orders?
- Which customers show high cancellation rates?

---

### Regions
- How does order volume and value vary by region?
- Are some regions more affected by cancellations?

---

### Cancellations analysis
- How do cancellations evolve over time?
- Are cancellations concentrated on specific products?
- Are cancellations higher for specific regions or customers?
- What patterns could explain cancellations?

---

## Key KPIs (high-level)

### Volume KPIs
- Total orders
- Delivered orders
- Cancelled orders
- Shipped orders
- Cancellation rate

---

### Financial KPIs
- Total order amount (delivered)
- Total order amount (cancelled)
- Total order amount (shipped)
- Month-over-month revenue growth

---

### Customer KPIs
- Number of active customers
- Orders per customer
- Average orders per customer

---

## Scope definition

### In scope
- Historical analysis of orders
- Product, customer, and regional breakdowns
- Trend and comparative analysis (MoM)

---

### Out of scope
- Real-time analytics
- Predictive modeling
- Detailed operational logistics
- Marketing attribution

---

## Assumptions
- One order has a single final status
- Order dates are reliable and complete
- Monetary values are stored in a single currency
- Historical data is immutable

All assumptions must be revisited if new information becomes available.

---

## Expected outcome
At the end of this project, the output should include:
- A clean and reliable analytical data model
- Clearly defined KPIs
- Reusable SQL queries
- Decision-oriented dashboards
- Documented assumptions and limitations

This document serves as a **reference point** for all subsequent project steps.
Any change in scope or objectives should be reflected here.
