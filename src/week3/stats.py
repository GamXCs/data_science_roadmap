import numpy as np
import pandas as pd
from numpy._core.strings import upper
from pandas._config.dates import pc_date_dayfirst_doc
from pandas.core.arrays import numeric


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


"""Running analysis on survival rate by group gives us a more accurate picture"""


def survival_rate_by_group(df: pd.DataFrame, column: str) -> pd.Series:
    """Return survival rate (mean of Survived) grouped by column"""
    return df.groupby(column)["Survived"].mean()


"""This function will inform us which numeric features are most strongly related to survival"""


def correlation_with_target(df: pd.DataFrame, target: str = "Survived") -> pd.Series:
    """Return correlation of each numeric column with the target, sorted by abs value"""

    # get the correlation (numerically) of the target
    corr = df.select_dtypes(include="number").corr()[target]

    # drop the target title since it is perfectly correlated with itself
    corr = corr.drop(target)

    # return the absolute value of categories
    return corr.abs().sort_values(ascending=False)


def detect_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """Detect outliers using the IQR (Interquartile Range) method. Returns count and % of outliers per column"""

    numeric_df = df.select_dtypes(include="number")
    results = {}

    for column in numeric_df.columns:
        q1 = numeric_df[column].quantile(0.25)
        q3 = numeric_df[column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outlier_mask = (numeric_df[column] < lower_bound) | (
            numeric_df[column] > upper_bound
        )
        outlier_count = outlier_mask.sum()
        outlier_pct = (outlier_count / len(numeric_df)) * 100

        results[column] = {"outlier_count": outlier_count, "outlier_pct": outlier_pct}
    return pd.DataFrame(results).T


if __name__ == "__main__":
    df = pd.read_csv("data/raw/titanic.csv")
    print(summarize_numeric(df))

    print(get_skewed_columns(df))

    print(survival_rate_by_group(df, "Pclass"))

    print(correlation_with_target(df))

    print(detect_outliers(df))
