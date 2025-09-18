"""
Onori EV dataset loader (stub).

Manual download:
- Place raw files under data/raw/onori/ (see data/README.md for links & license)
- Do NOT commit raw data.

Functions to implement later:
- load_capacity() -> pd.DataFrame
- load_hppc() -> pd.DataFrame
- load_eis() -> pd.DataFrame
- make_rul_labels(df_capacity, eol_capacity_frac=0.80) -> pd.DataFrame
"""
from pathlib import Path
import sys

RAW = Path("data/raw/onori")
SAMPLE = Path("data/sample/ev_rpt_sample.csv")

def main():
    if not RAW.exists():
        print("Raw data not found. Download to data/raw/onori/ and log checksums in data/README.md.")
    if SAMPLE.exists():
        print("Sample available: data/sample/ev_rpt_sample.csv (for notebook scaffolding).")
    else:
        print("No sample CSV found; create one at data/sample/ev_rpt_sample.csv to smoke-test notebooks.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
