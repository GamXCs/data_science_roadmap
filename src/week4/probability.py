from pathlib import Path

import pandas as pd

from week3.capstone import DATA_PATH


def empirical_probability(df: pd.DataFrame, column: str, value) -> float:
    pass


if __name__ == "__main__":
    DATA_PATH = "data/output/raw/titanic.csv"
    df = pd.read_csv(DATA_PATH)
