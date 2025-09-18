# Electric Vehicle Telemetry → Remaining Useful Life (RUL)

**One-sentence goal:** Predict the remaining useful life (RUL) of electric-vehicle lithium-ion cells from telemetry and diagnostic signals using supervised learning with transparent evaluation.

## Project Overview
- Frame RUL estimation as a regression problem that supports decision thresholds for maintenance planning.
- Engineer leak-free features from capacity, HPPC resistance, EIS spectra, and usage metadata collected during real-world EV-style cycling.
- Benchmark baseline linear models against tree-based ensembles with grouped cross-validation to respect per-cell structure.
- Deliver interpretable insights (feature importances, partial dependence, error analysis) and an accompanying video walk-through aligned with the course rubric.

## Data
Primary dataset: **Stanford Onori Lab — EV real-driving aging dataset (NMC, 21700 cells)**. The dataset captures urban dynamometer driving schedule (UDDS) discharge profiles, CC–CV charging at multiple C-rates, and scheduled reference performance tests (capacity, HPPC, EIS) for 10 cells aged over ~23 months at 23 °C.

- Landing page: [Bits & Watts Initiative](https://bitsandwatts.stanford.edu/publications/journal-article/lithium-ion-battery-aging-dataset-based-electric-vehicle-real-driving)
- Download & license: [OSF project (CC-BY 4.0)](https://osf.io/qsabn/?view_only=2a03b6c78ef14922a3e244f3d549de78)

Backup datasets to de-risk the plan:
1. [NASA PCoE Li-ion Battery Aging Datasets](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
2. [MIT–Stanford–TRI battery cycle-life dataset](https://www.tri.global/research/data-driven-prediction-battery-cycle-life-capacity-degradation)
3. [Kaggle EVIoT Predictive Maintenance](https://www.kaggle.com/datasets/datasetengineer/eviot-predictivemaint-dataset) (if an IoT table format is desired)

Refer to `data/README.md` for instructions on downloading and storing source files outside of version control.

## Remaining Useful Life Definition
- **End-of-Life (EOL) threshold:** 80% of initial rated capacity (standard industry practice). Adjust as needed if some cells do not cross the threshold; document any deviation.
- **RUL label:** For reference test index \(i\) occurring at cycle \(c_i\), define \(\text{RUL}_i = c_{\text{EOL}} - c_i\), where \(c_{\text{EOL}}\) is the first cycle at or below the EOL capacity.
- Optional binary framing: classify whether a cell will fail within the next \(N\) cycles (e.g., \(N = 100\)) to explore imbalanced classification metrics.

## Repository Structure
```
.
├── README.md
├── .gitignore
├── data/
│   ├── sample/              # tiny illustrative fragments (safe to commit)
│   └── README.md            # how to fetch raw data, licensing notes
├── notebooks/               # 01_clean_eda.ipynb, 02_modeling.ipynb, etc.
├── src/                     # reusable Python modules (data prep, features)
├── results/                 # exported figures/tables (kept small)
├── docs/
│   ├── project_plan.md      # milestone checklist derived from the blueprint
│   └── report_outline.md    # fill-in template for the final report
└── requirements.txt         # project dependencies pinned when finalized
```

## Planned Workflow
1. **Data acquisition & documentation** — cite sources, outline schema, freeze raw snapshots outside Git.
2. **Cleaning & exploratory analysis** — quantify missingness, validate labels, visualize degradation patterns.
3. **Feature engineering** — build capacity fade statistics, HPPC/EIS summaries, and stability metrics without leakage.
4. **Modeling & validation** — baseline regressors, tree ensembles, grouped/time-aware CV, systematic tuning.
5. **Evaluation & interpretation** — RMSE/MAE/\(R^2\), decision thresholds, permutation importance, residual analysis.
6. **Deliverables** — polished notebook/report, saved figures, 5–15 minute walkthrough video, README updates.

## Getting Started
1. Create and activate a Python 3.10+ environment (virtualenv, Conda, or uv).
2. Install requirements once finalized: `pip install -r requirements.txt`.
3. Download the Onori dataset per `data/README.md`; store raw files under `data/raw/` (ignored by Git).
4. Use the notebook naming convention `0X_topic.ipynb` for reproducible storytelling.

## Contribution Guidelines
- Keep raw data and large intermediate artifacts out of Git (use the ignored folders).
- Prefer readable, well-factored notebooks with Markdown summaries and conclusions.
- Add concise comments only where logic is non-obvious; favor self-documenting code otherwise.
- Update the project plan and report outline as milestones are completed.

## References
- Onori, S. et al. *Lithium-ion battery aging dataset based on electric vehicle real-driving profiles*. 2022. Bits & Watts Initiative, Stanford University.
- NASA Prognostics Center of Excellence. *Li-ion battery aging datasets*.
- Severson, K. A. et al. *Data-driven prediction of battery cycle life before capacity degradation*. Nature Energy, 2019.
