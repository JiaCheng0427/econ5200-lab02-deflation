# Index Integrity — Deflation, Substitution Bias & Goodhart
## Objective
This project studies how measurement choices can affect economic and product metrics, using CPI deflation, substitution bias, and Goodhart's Law.

## Methodology
- Diagnosed and fixed errors in a real-wage deflation function.
- Converted nominal wages into 2020 dollars using the average CPI for the base year.
- Compared CPI-U with Chained CPI (C-CPI-U).
- Measured the substitution gap using annual compounded inflation rates.
- Built a KPI monitoring example using DAU/MAU and time per session.
- Used rolling correlation to identify when the relationship between the two metrics became negative.
- Created a reusable `deflation_utils.py` module.
- Built an interactive index-integrity monitor with ipywidgets and Plotly.

## Key Findings
- CPI-U average annual inflation: about **2.61%**.
- C-CPI-U average annual inflation: about **2.35%**.
- The estimated upper-level substitution gap is about **0.27 percentage points per year**.
- The correlation between DAU/MAU and time per session changed from **+0.93** in the organic phase to **-0.96** in the gaming phase.- The interactive monitor detected the first negative rolling-correlation window around **Apr 2023–Sep 2023**.

## Files
- `lab-ch02-diagnostic.ipynb` — completed notebook
- `deflation_utils.py` — reusable deflation and profiling functions
