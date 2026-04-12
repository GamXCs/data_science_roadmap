import numpy as np
import pandas as pd


def create_series(data: list, index: list) -> pd.Series:
    """Create a Pandas Series from a list with a custom index"""
    return pd.Series(data, index=index)
