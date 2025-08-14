# further_exploration.py helper to test all possible ranges of CVSS Scores.
# src/severity.py
from typing import Optional, Union
import math

try:
    import pandas as pd
    from pandas.api.types import CategoricalDtype
except Exception:
    pd = None
    CategoricalDtype = None

ScoreLike = Union[float, int, str, None]

def _coerce_score(score: ScoreLike) -> Optional[float]:
    """Coerce various inputs to a float or return None."""
    if score is None:
        return None
    if isinstance(score, (float, int)):
        # handle NaN floats
        return None if (isinstance(score, float) and math.isnan(score)) else float(score)
    if isinstance(score, str):
        s = score.strip()
        if not s:
            return None
        try:
            v = float(s)
            return None if math.isnan(v) else v
        except ValueError:
            return None
    return None

def score_to_severity(score: ScoreLike) -> str:
    """
    Map a single CVSS v3.1 score to NVD bands:
      None: 0.0
      Low: 0.1–3.9
      Medium: 4.0–6.9
      High: 7.0–8.9
      Critical: 9.0–10.0
    Returns 'Unknown' for missing/invalid/out-of-range.
    """
    v = _coerce_score(score)
    if v is None:
        return "Unknown"
    if v == 0.0:
        return "None"
    if 0.0 < v <= 3.9:
        return "Low"
    if 4.0 <= v <= 6.9:
        return "Medium"
    if 7.0 <= v <= 8.9:
        return "High"
    if 9.0 <= v <= 10.0:
        return "Critical"
    return "Unknown"

def add_severity_band(df, score_col: str = "Score", out_col: str = "Severity"):
    """
    Pandas-based binning using pd.cut, matching score_to_severity bands.
    Mutates and returns df with an ordered categorical column `out_col`.
    """
    if pd is None:
        raise ImportError("pandas is required for add_severity_band")

    # Ensure numeric
    df[score_col] = pd.to_numeric(df[score_col], errors="coerce")

    bins   = [-0.001, 0.0, 3.9, 6.9, 8.9, 10.0]
    labels = ["None", "Low", "Medium", "High", "Critical"]

    ser = pd.cut(
        df[score_col],
        bins=bins,
        labels=labels,
        include_lowest=True,  # ensures 0.0 -> "None"
        right=True            # (a, b]
    )

    # Add "Unknown" category for NaNs or out-of-range (coerced to NaN)
    cat = CategoricalDtype(categories=labels + ["Unknown"], ordered=True)
    df[out_col] = ser.astype("category").cat.add_categories(["Unknown"]).fillna("Unknown").astype(cat)
    return df
