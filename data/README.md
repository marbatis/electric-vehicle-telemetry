# Data guide

## Source (primary)
- EV battery aging under real driving profiles (Onori Lab / OSF).
- Signals: periodic RPT (capacity, HPPC resistance, EIS), cycle index, test conditions.
- License: CC-BY (see dataset page). Do **not** commit raw data.

## Do not commit raw data
Place downloaded files under:


data/
raw/
onori/
# original files go here
sample/
ev_rpt_sample.csv


## Provenance log (fill after download)
| file | bytes | sha256 | acquired_on |
|------|-------|--------|-------------|
|      |       |        |             |

## Schema (high level)
- `cycle` (int) — diagnostic cycle index (RPT)
- `capacity_ah` (float) — measured capacity
- `resistance_mohm` (float) — HPPC-derived DC internal resistance
- `c_rate` (float) — nominal charge/discharge rate
- `temp_c` (float) — test temperature (°C)
- optionally `eis_*` — selected EIS summaries

## EOL & RUL labels
- EOL defined at 80% of initial capacity.
- For each RPT at cycle `c_i`, define `RUL_i = c_EOL - c_i` (compute using training data only to avoid leakage).
