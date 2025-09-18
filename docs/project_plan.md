# Project Plan: Electric Vehicle Telemetry -> Remaining Useful Life (RUL)

## Problem Definition
- **End-of-life (EOL) threshold:** 80% of each cell's initial rated capacity.
- **RUL label:** For reference performance test index \(i\) at cycle \(c_i\), compute \(\text{RUL}_i = c_{\text{EOL}} - c_i\), where \(c_{\text{EOL}}\) is the first cycle reaching ≤80% capacity. Restrict to cells crossing the threshold or adjust EOL (document if changed).
- **Task:** Supervised regression with optional thresholding for maintenance decisions; evaluate using RMSE, MAE, and supporting R^2.

## Feature Engineering Plan
- Capacity-based features: current capacity (Ah), percent fade vs. initial, rolling average change, last-k (3-5) capacity slopes.
- HPPC-derived features: charge/discharge resistance, delta resistance vs. baseline, temperature-adjusted resistance.
- EIS summaries: impedance magnitude at representative frequencies, real/imaginary parts at low/high frequency bands, Nyquist arc characteristics.
- Usage metadata: cycle index, elapsed days, charge/discharge C-rate, ambient temperature.
- Stability indicators: moving variance of capacity, Coulombic efficiency proxy, voltage recovery metrics.
- Interactions: capacity fade × resistance growth, C-rate × temperature.

## Data Splitting & Leakage Guard
- Grouped K-fold cross-validation (group = cell ID) to prevent data leakage across diagnostics of the same cell.
- Final hold-out: reserve at least one cell (e.g., EV10) as an untouched test set for final reporting.
- Time-awareness: within each cell, ensure train folds only include diagnostics up to the evaluation point (no future leakage).
- Random seeds locked in config; document any resampling or scaling performed inside cross-validation folds.

## Metrics & Evaluation Artifacts
- Primary metrics: RMSE, MAE.
- Secondary metric: R^2 to communicate explained variance.
- Decision support: threshold predictions at RUL < 100 cycles (or similar) to produce precision/recall/confusion matrix.
- Confidence reporting: include CV mean ± std across folds; optional bootstrap on hold-out cell.

## Figure & Table Checklist
- Missingness heatmap/bar chart for diagnostics.
- Capacity vs. cycle plots with 80% EOL line per cell.
- RUL distribution histogram.
- Correlation heatmap between engineered features and RUL.
- Model leaderboard table (CV mean ± std of RMSE/MAE/R^2).
- Parity plot (predicted vs. actual RUL) for validation and hold-out sets.
- Feature importance bar chart (permutation importance or SHAP summary).
- Residual plot segmented by cell or RUL band (optional but recommended).

## Milestones & Suggested Timeline
| Milestone | Focus | Key Outputs | Target Window |
| --- | --- | --- | --- |
| M1 | Dataset selection & repo scaffold | README, data citation, raw snapshot stored locally | Days 1-2 |
| M2 | Cleaning & exploratory analysis | Missingness summary, capacity trends, EDA notebook | Days 3-5 |
| M3 | Baseline + tree models | Baseline metrics, grouped CV setup, tuning grid | Days 6-8 |
| M4 | Model refinement & interpretation | Finalized model leaderboard, feature importances, error slices | Days 9-11 |
| M5 | Deliverables polish | Report/notebook ready, figures exported, environment pinned | Days 12-13 |
| M6 | Presentation | 5-15 minute video, README updated with results & links | Day 14 |

## Task Checklist
- [ ] Define and compute EOL/RUL labels per diagnostic checkpoint.
- [ ] Acquire Onori dataset (and backup if necessary); log provenance in `data/README.md`.
- [ ] Build loaders in `src/data/onori_loader.py` for capacity, HPPC, EIS, and label construction.
- [ ] Quantify missingness and outliers; choose imputation/outlier strategies.
- [ ] Produce EDA visuals (capacity vs. cycle, RUL distribution, correlation heatmap, HPPC vs. RUL).
- [ ] Engineer features listed above without leakage.
- [ ] Implement grouped/time-aware cross-validation and hold-out evaluation.
- [ ] Train baseline (mean, linear/elastic net) and tree-based models; document tuning results.
- [ ] Evaluate using RMSE/MAE/R^2; derive threshold-based metrics for maintenance decisions.
- [ ] Run permutation importance, partial dependence, and residual slicing for interpretability.
- [ ] Record video walkthrough covering problem -> data -> modeling -> results.
- [ ] Complete submission checklist before final handoff.

## Risks & Mitigations
- **Limited number of cells:** grouped CV by cell and uncertainty intervals; highlight generalization limits in discussion.
- **Incomplete degradation:** adjust EOL threshold or project RUL via trend fitting; document decisions.
- **Complex EIS data:** compute summary statistics or dimensionality reduction; park detailed analysis in appendix.
- **Overfitting risk:** start with simpler models, restrict feature count, apply regularization, and monitor train/test gaps.
