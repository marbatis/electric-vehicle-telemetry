# Electric Vehicle Telemetry → Remaining Useful Life (RUL)

Supervised regression project to estimate **remaining useful life (RUL)** of EV lithium-ion cells using the Stanford Onori Lab telemetry and diagnostic dataset. The work targets preventative maintenance decisions by forecasting cycles-to-failure, evaluated with **RMSE**, **MAE**, and supporting **R²**.

## Why It Matters
- EV battery RUL estimation unlocks informed warranty, maintenance scheduling, and safety interventions.
- Open, reproducible pipeline aligned to an academic rubric, using publicly documented diagnostic measurements.
- Emphasis on leak-free feature engineering, grouped cross-validation, and interpretable tree-based models.

## Data Sources
Primary dataset: **Stanford Onori Lab — EV real-driving aging dataset (NMC, 21700 cells)**
- Real urban drive-cycle (UDDS) discharge, CC–CV charging, 10 cells, aged over ~23 months at 23 °C.
- Periodic reference performance tests (RPT) providing capacity checks, hybrid pulse power characterization (HPPC), and electrochemical impedance spectroscopy (EIS).
- Landing page: [Bits & Watts Initiative](https://bitsandwatts.stanford.edu/publications/journal-article/lithium-ion-battery-aging-dataset-based-electric-vehicle-real-driving)
- Download & license: [OSF project (CC-BY 4.0)](https://osf.io/qsabn/?view_only=2a03b6c78ef14922a3e244f3d549de78)

Backup datasets to de-risk the plan:
1. [NASA PCoE Li-ion Battery Aging Datasets](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
2. [MIT–Stanford–TRI battery cycle-life dataset](https://www.tri.global/research/data-driven-prediction-battery-cycle-life-capacity-degradation)
3. [Kaggle EVIoT Predictive Maintenance](https://www.kaggle.com/datasets/datasetengineer/eviot-predictivemaint-dataset)

For acquisition instructions, schema notes, and provenance logging, see `data/README.md`.

## Run Order
1. `notebooks/01_clean_eda.ipynb` – clean raw diagnostics, construct RUL labels, and perform guided EDA.
2. `notebooks/02_models_cv.ipynb` – implement grouped splits, baselines, tree ensembles, tuning, and interpretation.
3. `notebooks/03_report.ipynb` – narrative summary notebook aggregating findings, figures, and conclusions.

## Project Structure
```
.
├── README.md
├── .gitignore
├── data/
│   ├── sample/              # tiny illustrative fragments (safe to commit)
│   └── README.md            # acquisition instructions & provenance log
├── docs/
│   ├── project_plan.md      # milestone checklist & modeling specs
│   ├── report_outline.md    # report template aligned to rubric
│   ├── submission_checklist.md
│   └── video_outline.md
├── notebooks/               # 01_clean_eda.ipynb, 02_models_cv.ipynb, 03_report.ipynb
├── results/                 # exported figures/tables (kept small)
├── src/
│   └── data/onori_loader.py # data access stubs & usage guidance
├── requirements.txt         # environment seed (pin later)
└── Makefile                 # convenience commands (setup, clean, notebook entry)
```

## Planned Workflow
1. **Problem framing** — document supervised RUL regression target and decision thresholds.
2. **Data acquisition & documentation** — cite sources, outline schema, track provenance without storing raw files in Git.
3. **Cleaning & exploratory analysis** — quantify missingness/outliers, validate labels, visualize degradation.
4. **Feature engineering** — derive capacity fade metrics, HPPC resistance deltas, EIS summaries, stability indicators.
5. **Modeling & validation** — run baselines and tree ensembles with grouped cross-validation by cell and a hold-out cell test.
6. **Evaluation & interpretation** — report RMSE/MAE/R², decision-oriented thresholds, permutation importance, residual slices.
7. **Deliverables** — polished notebook/report, saved figures, 5–15 minute walkthrough video, README and submission checklist updates.

## Rubric Map (where to find things)
- **Project topic & goal** → README (top) · `notebooks/03_report.ipynb` §Problem & Goal
- **Data (cited & described)** → README §Data Sources · `data/README.md`
- **Cleaning** → `notebooks/01_clean_eda.ipynb` · `docs/report_outline.md` §4
- **EDA** → `notebooks/01_clean_eda.ipynb` · `docs/report_outline.md` §5
- **Models (multiple + CV/tuning)** → `notebooks/02_models_cv.ipynb` · `docs/report_outline.md` §7
- **Results & analysis** → `notebooks/02_models_cv.ipynb` · `docs/report_outline.md` §8
- **Interpretability & error analysis** → `notebooks/02_models_cv.ipynb` · `docs/report_outline.md` §9
- **Discussion & conclusion** → `notebooks/03_report.ipynb` §Discussion
- **Video (5–15 min)** → `docs/video_outline.md`
- **Public GitHub organization/comments** → this repository · `docs/submission_checklist.md`

## Getting Started
1. Create and activate a Python 3.10+ environment (virtualenv, Conda, or uv).
2. Install shared dependencies: `pip install -r requirements.txt` (pin exact versions once the environment is stable).
3. Download the Onori dataset per `data/README.md`; store raw files under `data/raw/` (ignored by Git).
4. Duplicate the notebook templates and execute in order, committing only evaluated notebooks that run top-to-bottom.
5. Update `docs/submission_checklist.md` as deliverables complete.

## Contribution Guidelines
- Keep raw data, large intermediates, and secrets out of Git; use ignored folders under `data/` and `results/`.
- Prefer readable notebooks with Markdown conclusions and restrained code comments.
- Document non-obvious decisions in `docs/project_plan.md`, commit frequently, and tag releases at major milestones.

## References
- Onori, S. et al. *Lithium-ion battery aging dataset based on electric vehicle real-driving profiles*. 2022. Bits & Watts Initiative, Stanford University.
- NASA Prognostics Center of Excellence. *Li-ion battery aging datasets*.
- Severson, K. A. et al. *Data-driven prediction of battery cycle life before capacity degradation*. Nature Energy, 2019.
