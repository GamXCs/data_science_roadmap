from pathlib import Path

import pandas as pd


def empirical_probability(df: pd.DataFrame, column: str, value) -> float:
    # check if column is empty
    if column not in df.columns:
        return 0.0
    if len(df) == 0:  # check if the dataframe is empty
        return 0.0
    return len(df[df[column] == value]) / len(df)


if __name__ == "__main__":
    DATA_PATH = "data/output/raw/titanic.csv"
    df = pd.read_csv(DATA_PATH)
