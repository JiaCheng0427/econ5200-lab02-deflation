"""Deflation utilities for ECON 5200 labs."""

import pandas as pd


def deflate_series(nominal, cpi, base_year=2020):
    """Convert a nominal time series to real (constant-dollar) values.

    Parameters
    ----------
    nominal : pd.Series
        Nominal values indexed by date.
    cpi : pd.Series
        CPI values indexed by date.
    base_year : int
        Year whose dollars to express values in.

    Returns
    -------
    pd.Series
        Real values in base-year dollars, with no missing values.
    """

    if not (cpi.index.year == base_year).any():
        raise ValueError(f"Base year {base_year} not found in CPI data.")

    base_cpi = cpi[cpi.index.year == base_year].mean()

    aligned = pd.concat(
        [nominal.rename("nominal"), cpi.rename("cpi")],
        axis=1,
        join="inner"
    ).dropna()

    if aligned.empty:
        raise ValueError("nominal and cpi have no overlapping observations")

    real = (aligned["nominal"] / aligned["cpi"]) * base_cpi

    return real


def profile_dataframe(data, unit_col="name", time_col="date"):
    """Create a basic profile of a panel-style DataFrame."""

    profile = {}

    profile["shape"] = data.shape
    profile["n_units"] = data[unit_col].nunique()
    profile["n_periods"] = data[time_col].nunique()

    periods_per_unit = data.groupby(unit_col)[time_col].nunique()

    complete = periods_per_unit[
        periods_per_unit == profile["n_periods"]
    ]

    profile["n_complete_units"] = len(complete)
    profile["balanced"] = len(complete) == profile["n_units"]

    missing = {}

    for col in data.columns:
        missing[col] = data[col].isna().mean() * 100

    profile["missing_pct"] = missing

    return profile