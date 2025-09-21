# EV Battery RUL — Results Summary

**Problem/Goal** — Supervised **regression** to predict Remaining Useful Life (RUL) in **diagnostic steps remaining** to 80% EOL.  
**Why** — enable planned maintenance before performance drops.

**Data** — Onori EV aging (Diag_*/Capacity_test), **101 diagnostics / 10 cells**. Capacity per diagnostic from Excel; EOL = 0.8 × initial per cell.  
**Features** — `diag`, `capacity_ah`, **fade_frac** = 1 − cap/cap0, **cap_slope_k3** (short-window slope), plus `c_rate`/`temp_c` parsed from filenames.

**Cleaning/EDA** — label construction; RUL histogram; capacity/fade vs diagnostic index; figures in `results/figs/`.

**Models & Evaluation** — Grouped CV by `cell_id` (leave-one-cell-out style). Models: baseline mean, **diag-only LinearRegression**, **Elastic Net**, **RandomForest**, **HistGradientBoosting**, **SVR (RBF)**.  
**Leaderboard** — see `results/leaderboard.csv`.  
**Tuned Elastic Net (poly, filtered ≥5 diags)** — **OOF**: RMSE ≈ **1.35**, MAE ≈ **0.88**, R² ≈ **0.89**; `results/per_cell_oof_metrics_tuned.csv`, parity plot in `results/figs/`.

**Interpretability** — standardized coefficients: `diag` (−), `capacity_ah` (+), `fade_frac` (+), slope (+): aligns with battery physics.

**Limits & Next** — only 10 cells; fixed temp; RUL in diagnostics. Next: add HPPC ΔR, try quantile regression, expand cells/temps.
