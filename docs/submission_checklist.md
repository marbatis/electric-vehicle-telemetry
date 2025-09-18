# Submission Checklist

Use this checklist before final handoff to confirm rubric requirements are satisfied.

## Core Deliverables
- [ ] README states supervised regression goal, metrics (RMSE/MAE/R^2), and dataset citations.
- [ ] Notebooks executed in order (`01_clean_eda` -> `02_models_cv` -> `03_report`) with outputs committed.
- [ ] `docs/report_outline.md` populated or exported as final PDF.
- [ ] Video recorded (5-15 minutes) and linked in README + this checklist.

## Data & Provenance
- [ ] `data/README.md` updated with actual files, checksums, and any preprocessing notes.
- [ ] Raw data stored under `data/raw/` (ignored by Git); samples remain small.
- [ ] Provenance table completed with download dates and SHA256 hashes.

## Cleaning & EDA
- [ ] Missingness analysis documented with visual.
- [ ] Capacity vs. cycle plot with 80 percent EOL line per cell.
- [ ] RUL distribution histogram and HPPC vs. RUL insight captured.
- [ ] Insight log completed in `01_clean_eda.ipynb`.

## Modeling & Evaluation
- [ ] Grouped cross-validation by cell implemented and described.
- [ ] Baselines (mean, linear/elastic net) and tree-based models (RF, GBM) evaluated.
- [ ] Leaderboard table filled with CV mean ± std for RMSE/MAE/R^2.
- [ ] Hold-out evaluation with parity plot and thresholded decision metrics.
- [ ] Permutation importance and partial dependence (or ALE) generated.
- [ ] Residual/error slices reviewed and captured in notebooks.

## Documentation & Repo Hygiene
- [ ] `docs/project_plan.md` updated to reflect implemented decisions.
- [ ] README run order matches final notebooks.
- [ ] `requirements.txt` pinned with exact versions used.
- [ ] Makefile targets verified on clean environment.
- [ ] LICENSE, CITATION.cff, issue/PR templates present and correct.
- [ ] CI (codespell + gitleaks) passing on latest commit.

## Final Packaging
- [ ] Tag release with final version and include summary of results.
- [ ] Upload final figures to `results/` (lightweight) and reference in report.
- [ ] Provide video link and any external assets in README and this checklist.
- [ ] Run `git status` to confirm clean working tree before submission.
