# Data Directory

This repository does **not** contain the full raw datasets. Use the instructions below to retrieve the required files and place them in the appropriate subfolders.

## Folder Convention
- `data/raw/` – untouched source files downloaded from OSF or alternate providers (ignored by Git).
- `data/interim/` – cleaned/intermediate artifacts saved during processing (ignored by Git).
- `data/processed/` – modeling-ready tables or feature matrices (ignored by Git).
- `data/sample/` – tiny, anonymized examples that demonstrate file formats and allow notebooks to run quickly without the full dataset.

Create directories as needed; only `data/sample/` is tracked to keep the repo lightweight.

## Primary Dataset: Stanford Onori Lab EV Aging
1. Visit the [Bits & Watts Initiative page](https://bitsandwatts.stanford.edu/publications/journal-article/lithium-ion-battery-aging-dataset-based-electric-vehicle-real-driving) for context.
2. Download from the [OSF project](https://osf.io/qsabn/?view_only=2a03b6c78ef14922a3e244f3d549de78). The project provides diagnostic measurements (capacity tests, HPPC, EIS) and cycling data for 10 NMC 21700 cells aged under EV-style drive cycles.
3. Store the raw archives or CSV files in `data/raw/`. Keep the original filenames for provenance.
4. Document any preprocessing decisions in your notebooks and update this README if new resources are added.

## Backup Datasets
If substituting or augmenting with alternative datasets, place them under `data/raw/<dataset-name>/` and cite:
- [NASA PCoE Li-ion battery aging datasets](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [MIT–Stanford–TRI battery cycle-life dataset](https://www.tri.global/research/data-driven-prediction-battery-cycle-life-capacity-degradation)
- [Kaggle EVIoT Predictive Maintenance dataset](https://www.kaggle.com/datasets/datasetengineer/eviot-predictivemaint-dataset)

## Data Handling Checklist
- Verify units (capacity in Ah, resistance in mΩ, temperature in °C).
- Record download dates and versions for reproducibility.
- Avoid committing files larger than a few megabytes; link to the original source instead.
