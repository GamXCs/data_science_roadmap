import numpy as np
import pandas as pd


def summarize_numeric(df: pd.DataFrame) -> pd.DataFrame:
    """Return descriptive stats for all numeric columns"""
    numeric_df = df.select_dtypes(include="number")
    stats = numeric_df.describe()
    stats.loc["skewness"] = numeric_df.skew()
    stats.loc["kurtosis"] = numeric_df.kurt()
    return stats


# extract skewness
def get_skewed_columns(df: pd.DataFrame, threshold: float = 1.0) -> list:
    """Return column names where absolute skewness exceeds threshold"""
    # get the columns with numeric values
    numeric_df = df.select_dtypes(include="number")
    skewness = numeric_df.skew()  # get skewed cols
    skewed = skewness[skewness.abs() > threshold]
    return skewed.index.tolist()


if __name__ == "__main__":
    df = pd.read_csv("data/raw/titanic.csv")
    print(summarize_numeric(df))

    print(get_skewed_columns(df))
