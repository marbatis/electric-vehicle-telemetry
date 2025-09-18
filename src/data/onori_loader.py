"""Utility stubs for accessing the Stanford Onori EV battery aging dataset.

These functions intentionally raise NotImplementedError until the raw data files
are downloaded (see `data/README.md`). They document the expected inputs and
outputs so implementation is straightforward once datasets are in place.
"""

from __future__ import annotations
from pathlib import Path
from typing import Optional

DATA_ROOT = Path("data/raw/onori_ev")


def load_capacity(path: Optional[Path] = None):
    """Load reference performance test (RPT) capacity measurements.

    Parameters
    ----------
    path:
        Optional override of the base directory containing capacity CSV files.

    Returns
    -------
    pandas.DataFrame
        Expected columns include `cell_id`, `cycle_index`, `capacity_ah`,
        `temperature_c`, and timestamps. Implementers should ensure data types
        are numeric where appropriate and attach metadata for provenance.
    """

    raise NotImplementedError("Implement once capacity files are downloaded.")


def load_hppc(path: Optional[Path] = None):
    """Load Hybrid Pulse Power Characterization (HPPC) resistance data.

    Expected output schema should include `cell_id`, `cycle_index`, state-of-
    charge information, pulse durations, and charge/discharge resistance
    measurements derived from the diagnostic tests.
    """

    raise NotImplementedError("Implement once HPPC files are downloaded.")


def load_eis(path: Optional[Path] = None):
    """Load Electrochemical Impedance Spectroscopy (EIS) measurements.

    Implementations should return frequencies (Hz), real/imag impedance
    components, and any metadata needed to align with capacity/HPPC tests.
    Consider summarizing spectra into feature-ready representations upstream of
    modeling to control dimensionality.
    """

    raise NotImplementedError("Implement once EIS files are downloaded.")


def make_rul_labels(capacity_df, eol_capacity: float = 0.8):
    """Generate RUL targets from capacity diagnostics.

    Parameters
    ----------
    capacity_df:
        DataFrame produced by `load_capacity` with at least `cell_id`,
        `cycle_index`, and `capacity_ah` columns.
    eol_capacity:
        Fraction of the initial capacity considered end-of-life (default 0.8).

    Returns
    -------
    pandas.DataFrame
        Input frame augmented with `initial_capacity_ah`, `capacity_fraction`,
        `cycle_eol`, and `rul_cycles` columns. Ensure calculations use only
        historical information per row to avoid leakage.
    """

    raise NotImplementedError("Implement RUL label creation after cleaning.")


if __name__ == "__main__":
    print(
        "Download the Onori dataset per data/README.md and place files under "
        f"{DATA_ROOT} before implementing loader functions."
    )
