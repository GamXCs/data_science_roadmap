from pathlib import Path

import pandas as pd


def empirical_probability(df: pd.DataFrame, column: str, value) -> float:
    # check if column is empty
    if column not in df.columns:
        return 0.0
    if len(df) == 0:  # check if the dataframe is empty
        return 0.0
    return len(df[df[column] == value]) / len(df)


"""This function will model P(A|B) which is the probability
of A, given that B is true
Step 1: Narrow down the df to only rows where B is true
Step 2: Compute probability of A within that group
Ex: Titanic dataset -P(Survived | Sex == 'female') means:
    out of all the female passengers, how many survived
    P(A | B) = P(A and B) / P(B)"""


def conditional_probability(df, col_a, val_a, col_b, val_b):
    if col_b not in df.columns:
        return 0.0
    filtered_df = df[df[col_b] == val_b]
    return empirical_probability(filtered_df, col_a, val_a)


if __name__ == "__main__":
    DATA_PATH = "data/output/raw/titanic.csv"
    df = pd.read_csv(DATA_PATH)
