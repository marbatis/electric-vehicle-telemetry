# Video Outline (10-minute target)

## 0:00 - 0:20 — Hook
- Why EV battery RUL matters for reliability, warranty, and safety.

## 0:20 - 1:30 — Problem & Objective
- State the supervised regression goal (predict cycles-to-failure).
- Mention metrics (RMSE, MAE, R^2) and decision threshold for maintenance.

## 1:30 - 3:00 — Data Overview
- Cite the Onori EV dataset (UDDS drive cycle, CC-CV charge, 10 cells, diagnostics).
- Highlight data schema: capacity, HPPC, EIS, cycling traces.
- Mention provenance tracking (data/README.md) and licensing.

## 3:00 - 5:00 — Cleaning & EDA Highlights
- Show missingness summary and capacity vs. cycle with 80 percent EOL line.
- Discuss RUL distribution and correlation heatmap insights.
- Call out HPPC resistance trends and any EIS summaries.

## 5:00 - 7:00 — Modeling Strategy
- Describe grouped cross-validation (by cell) and hold-out cell choice.
- Walk through baselines (mean, linear/elastic net) and tree ensembles (RF, GBM).
- Summarize tuning approach and leaderboard table structure.

## 7:00 - 8:30 — Results & Interpretation
- Present CV metrics (RMSE/MAE/R^2) and hold-out parity plot.
- Show thresholded decision metrics (e.g., precision/recall at RUL < 100 cycles).
- Share permutation importance and partial dependence highlights.

## 8:30 - 9:30 — Error Analysis & Limitations
- Discuss residual slices by cell/C-rate, failure cases, and uncertainty.
- Mention small-sample risk and mitigation notes.

## 9:30 - 10:00 — Wrap-Up & Next Steps
- Reiterate impact, recommended deployment steps, and potential extensions (NASA backups, early-cycle prognosis).
- Point viewers to the README, notebooks, and submission checklist for replication.
