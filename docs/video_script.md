# Video Script (≈10 minutes)

**Slide 1 — Title (20s)**  
We predict EV battery Remaining Useful Life (RUL) in diagnostic steps remaining to 80% EOL.

**Slide 2 — Problem & Goal (40s)**  
Why it matters; RUL definition; supervised regression task.

**Slide 3 — Data (60s)**  
Onori EV capacity tests; 101 diagnostics across 10 cells; EOL rule; derived features.

**Slide 4 — Cleaning/EDA (120s)**  
Show RUL histogram; capacity/fade vs diagnostic index; mention takeaways.

**Slide 5 — Models & CV (120s)**  
Grouped CV by `cell_id`; models compared (baseline mean, diag-only LR, EN, RF, HGBM, SVR); metrics.

**Slide 6 — Leaderboard (90s)**  
Briefly compare models; linear diag only and EN are competitive on this small monotonic dataset.

**Slide 7 — Tuned OOF (120s)**  
Elastic Net + polynomial features, filtered to cells with ≥5 diags: OOF RMSE≈1.35, MAE≈0.88, R²≈0.89; parity plot.

**Slide 8 — Interpretability (60s)**  
Coefficients: `diag` (−), `capacity_ah` (+), `fade_frac` (+), slope helps; physics-aligned.

**Slide 9 — Limits & Next (50s)**  
Few cells; fixed temp; RUL in diagnostics; next: HPPC ΔR, quantile regression, more cells/temps.

**Close (20s)**  
Repo link and slides; thank you.
