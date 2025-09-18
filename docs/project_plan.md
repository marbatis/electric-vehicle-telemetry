# Project Plan: Electric Vehicle Telemetry → Remaining Useful Life (RUL)

## Milestones & Suggested Timeline
| Milestone | Focus | Key Outputs | Target Window |
| --- | --- | --- | --- |
| M1 | Dataset selection & repo scaffold | README, data citation, raw snapshot stored locally | Days 1–2 |
| M2 | Cleaning & exploratory analysis | Missingness summary, capacity trends, EDA notebook | Days 3–5 |
| M3 | Baseline + tree models | Baseline metrics, grouped CV setup, tuning grid | Days 6–8 |
| M4 | Model refinement & interpretation | Finalized model leaderboard, feature importances, error slices | Days 9–11 |
| M5 | Deliverables polish | Report/notebook ready, figures exported, environment pinned | Days 12–13 |
| M6 | Presentation | 5–15 minute video, README updated with results & links | Day 14 |

## Task Checklist
- [ ] Define RUL/EOL thresholds and document them.
- [ ] Acquire Onori dataset (and backup if necessary); log provenance.
- [ ] Build data loading helpers in `src/` (schema validation, type enforcement).
- [ ] Quantify missingness and outliers; choose imputation/outlier strategies.
- [ ] Create EDA visuals (capacity vs. cycle, RUL distribution, correlation heatmap, HPPC vs. RUL).
- [ ] Engineer leak-free features (capacity fade, resistance deltas, EIS summaries, stability metrics).
- [ ] Implement grouped/time-aware cross-validation to avoid leakage between cells.
- [ ] Train baseline (mean, linear) and tree-based models; tune with systematic search.
- [ ] Evaluate with RMSE/MAE/R²; derive decision thresholds and classification metrics if needed.
- [ ] Run permutation importance and partial dependence for interpretability.
- [ ] Perform residual/error analysis and document insights.
- [ ] Record video walkthrough covering problem → data → modeling → results.

## Risks & Mitigations
- **Limited number of cells:** use grouped CV by cell and report uncertainty intervals.
- **Incomplete degradation:** adjust EOL threshold or predict capacity at next RPT to derive RUL; explain clearly.
- **Complex EIS features:** reduce dimensionality via summary statistics or feature selection.
- **Overfitting to diagnostic points:** start simple, regularize, and monitor performance gaps between train/test cells.

Update this plan as milestones are completed to maintain alignment with deliverables and grading rubric.
