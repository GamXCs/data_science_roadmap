import numpy as np
import pandas as pd


def fill_missing_values(df: pd.DataFrame, column: str, fill_value) -> pd.DataFrame:
    """Fill missing values in a column with a given value"""
    df[column] = df[column].fillna(fill_value)
    return df


def drop_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Drop all rows that contain at least one missing value"""
    return df.dropna()
