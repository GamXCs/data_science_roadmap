from pathlib import Path

import pandas as pd


def empirical_probability(df: pd.DataFrame, column: str, value) -> float:
    # check if column exists
    if column not in df.columns:
        return 0.0
    if len(df) == 0:  # check if the dataframe is empty
        return 0.0
    return len(df[df[column] == value]) / len(df)


def conditional_probability(df, col_a, val_a, col_b, val_b):
    """Return P(A | B): the probability of A given that B is true.

    Step 1: narrow df to the rows where B is true.
    Step 2: compute the probability of A within that group.

    Example (Titanic): P(Survived == 1 | Sex == 'female') is the share
    of female passengers who survived.

    P(A | B) = P(A and B) / P(B)
    """
    if col_b not in df.columns:
        return 0.0
    filtered_df = df[df[col_b] == val_b]
    return empirical_probability(filtered_df, col_a, val_a)


def bayes_theorem(p_a, p_b_given_a, p_b):
    """Bayes formula: P(B|A) * P(A) / P(B)"""

    if p_b == 0:
        return 0.0
    return p_b_given_a * p_a / p_b


def expected_value(outcomes, probabilities):
    """Return the expected value: the sum of each outcome times its probability.
    Returns 0.0 if the lists differ in length."""

    if len(outcomes) != len(probabilities):
        return 0.0

    outcome_val = 0.0
    for outcome, probability in zip(outcomes, probabilities):
        outcome_val += outcome * probability
    return outcome_val


def probability_distribution(df, column):
    """Return a dict mapping each unique value in column to its probability.

    Returns {} if the column is missing or the DataFrame is empty.
    """
    # check for empty column and return empty dict
    if column not in df.columns or len(df) == 0:
        return {}

    emp_dict = {}
    for val in df[column].unique():
        emp_dict[val] = empirical_probability(df, column, val)
    return emp_dict


if __name__ == "__main__":
    DATA_PATH = "data/raw/titanic.csv"
    df = pd.read_csv(DATA_PATH)

    print(df["Pclass"].unique())
    print(probability_distribution(df, "Pclass"))
    print(sum(probability_distribution(df, "Pclass").values()))
    print()
    print(df["Pclass"].value_counts(normalize=True))
