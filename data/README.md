# Data Directory

This repository documents how to retrieve and prepare electric-vehicle battery telemetry for the RUL study. **Raw datasets are not versioned**; only tiny illustrative samples live under `data/sample/`.

## Source & Licensing
- **Primary dataset:** Stanford Onori Lab — EV real-driving aging dataset (NMC, 21700 cells).
  - Context & citation: [Bits & Watts Initiative](https://bitsandwatts.stanford.edu/publications/journal-article/lithium-ion-battery-aging-dataset-based-electric-vehicle-real-driving)
  - Download: [OSF project](https://osf.io/qsabn/?view_only=2a03b6c78ef14922a3e244f3d549de78)
  - License: Creative Commons Attribution 4.0 International (CC-BY 4.0). Respect attribution requirements in reports and presentations.
- **Backups:** NASA PCoE Li-ion battery aging datasets, MIT–Stanford–TRI battery cycle-life dataset, and Kaggle EVIoT Predictive Maintenance. Use them only if the primary source is unavailable; cite accordingly.

## Expected Folder Layout (ignored by Git)
```
data/
├── raw/
│   └── onori_ev/
│       ├── metadata/
│       ├── cycling/
│       ├── rpt_capacity/
│       ├── rpt_hppc/
│       └── rpt_eis/
├── interim/
├── processed/
└── sample/
```
- `data/raw/onori_ev/` — untouched downloads from OSF (rename folders minimally for clarity).
- `data/interim/` — intermediate tables, cleaned diagnostics, temporary joins.
- `data/processed/` — modeling-ready features, train/test splits, metrics exports.
- `data/sample/` — lightweight CSV/JSON snippets checked into Git for quick notebook demos.

## Dataset Overview
| Aspect | Description |
| --- | --- |
| Cells | 10 cylindrical 21700 NMC cells aged at 23 °C |
| Cycling profile | Urban Dynamometer Driving Schedule (UDDS) discharge; CC–CV charge at multiple C-rates |
| Duration | ~23 months of cycling with periodic diagnostics |
| Diagnostics | Reference Performance Tests (RPT) capturing capacity, HPPC pulse resistance, and EIS spectra |
| Files | Separate CSV/Matlab files per diagnostic modality plus metadata logs |

Use this schema to design loaders:
- **Capacity RPT** — cycle index, measured capacity (Ah), voltage limits, temperature.
- **HPPC** — state of charge, pulse duration, charge/discharge resistance values.
- **EIS** — frequency (Hz), real/imaginary impedance, phase angle.
- **Cycling logs** — timestamped current/voltage/temperature traces for drive cycles.

## Provenance Log
Track downloads for reproducibility. Update the table as files are added.

| Filename | Bytes | Checksum (SHA256) | Download date |
| --- | --- | --- | --- |
| *(add entries when files are saved under `data/raw/`)* |  |  |  |

Suggested command to compute a checksum:
```
shasum -a 256 <filename>
```

Record any preprocessing (unzip, renaming, conversion) in this file and in your notebooks.

## Acquisition Steps
1. Create `data/raw/onori_ev/` (or similar) locally.
2. Visit the OSF project link, download the archives for cycling, RPT capacity, HPPC, and EIS components.
3. Store the original archives and extracted CSVs/MAT files under `data/raw/onori_ev/`.
4. Log each file in the provenance table, including checksum and download date.
5. Optional: obtain the NASA or TRI backups and store them under `data/raw/<dataset-name>/`, logging entries here.

## Sample Data
The `data/sample/` directory contains tiny synthetic fragments to let notebooks run without the full dataset. Extend or regenerate samples as you build loaders, keeping them anonymized and <10 KB where possible.
