import numpy as np
import pandas as pd


def fill_missing_values(df: pd.DataFrame, column: str, fill_value) -> pd.DataFrame:
    """Fill missing values in a column with a given value"""
    df[column] = df[column].fillna(fill_value)
    return df


def drop_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Drop all rows that contain at least one missing value"""
    return df.dropna()


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Drop duplicate rows from a DataFrame"""
    return df.drop_duplicates()


def rename_columns(df: pd.DataFrame, rename_map: dict) -> pd.DataFrame:
    """Rename columns using a dictionary mapping old names to new names"""
    return df.rename(columns=rename_map)


def change_dtype(df: pd.DataFrame, column: str, dtype) -> pd.DataFrame:
    """Convert a column to a different data type"""
    df[column] = df[column].astype(dtype)
    return df


def strip_whitespace(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Strip leading and trailing whitespace from a string column"""
    df[column] = df[column].str.strip()
    return df
