# Sample Superstore: Sales, Profitability and Business Performance Analysis

A Power BI dashboard and an independent, evidence-based analysis of where a US/Canada office-products retailer makes and loses money.

#### Full report: `` Superstore_Analysis_Report.pdf `` (editable version: ` Superstore_Analysis_Report.docx `)

## Business problem

The business is growing quickly, but growth does not guarantee profit. This project asks which products, regions, customers and discount decisions create profit, and which destroy it, and what management should change.

#### Objectives
+ Track sales, profit, margin, orders, customers and average order value over time.
+ Find the categories, sub-categories and products that drive or erode profit.
+ Locate under-performing regions, states and cities.
+ Separate large customers from genuinely profitable customers.
+ Test how discounts relate to profitability.
+ Check whether shipping mode or speed affects profit.
#### Dataset
+ `samplesuperstore.csv`: 10,194 order line items, 26 columns, 5,111 orders, 804 customers, 1,849 products.
+ Order dates 3 Jan 2023 to 30 Dec 2026 (re-dated sample data), United States and Canada.
+ Fields: order, customer, geography, product, ship mode, Sales, Quantity, Discount, Profit.
+ Source: Sample Superstore dataset. (Add the exact download link and licence before publishing.)
#### Tools and technologies
+ Power BI Desktop: data model, 7 DAX measures, 7-page interactive dashboard with Year/Quarter/Month slicers.
+ DAX: `DIVIDE`, `DISTINCTCOUNT`, `DATEDIFF`.
+ Python (pandas, matplotlib): independent recomputation of KPIs from the raw CSV `(superstore_analysis.py)`.
#### Methodology
1. Inspected the data: no missing values; checked duplicates and customer-ID consistency.
2. Reconciled every dashboard KPI against values recomputed from the CSV (all match).
3. Analysed trends, contribution by category/region/segment, customer concentration, discount tiers and shipping.
4. Treated correlations as association, not causation; labelled findings as verified, interpretation or hypothesis.
#### Key findings
| Finding	| Evidence |
| :--- | :--- |
| Overall performance |	$2.33M sales, $292.3K profit, 12.56% margin; sales +58% from 2024 to 2026 |
| Deep discounts destroy profit |	1,415 lines discounted 30%+ lost $136.0K; 96.8% loss-making; lines at 20% or less earned a 21.8% margin |
| Furniture is the weak category | 32.4% of sales but 6.7% of profit (2.61% margin); Tables lose $17.8K |
| Central region under-earns |	7.9% margin vs 15.0% in the West; Texas -$25.7K, Illinois -$12.6K |
| Revenue is not profit	| Top-revenue customer is a net loss; 159 of 804 customers are unprofitable |
| Shipping is not a profit lever |	Ship-mode margins 12.2% to 13.9%; average dispatch 3.96 days |
#### Recommendations (all potential, untested)
1. Tiered discount approval: standard up to 20%, manager sign-off 20 to 30%, executive exception above 30%.
2. Discount and pricing review in Texas, Illinois, Ohio and Pennsylvania.
3. Reprice or cap discounts on Tables, Bookcases and Machines; set price floors for the ten worst products.
4. Margin checks on large quotes; review loss-making customer accounts.
5. Plan the Q4 peak (37% to 39% of sales each year) with a discount budget.
Dashboard screenshots to include

#### Limitations and future improvements
+ No cost, freight, returns or delivery-date data; Shipping Days measures order-to-dispatch time.
+ The CSV discount column appears rounded to one decimal compared with the dashboard model.
+ Dates run past the report date, so trends describe the dataset only.
+ Next: test a discount cap with a controlled pilot, add shipping cost and delivery dates, cohort/repeat-purchase analysis, and fix the dashboard design issues listed in the report (Top-N filters hiding losses, map legend, funnel chart, discount scatter totals).
