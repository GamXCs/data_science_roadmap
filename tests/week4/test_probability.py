import pandas as pd
import pytest

from src.week4.probability import empirical_probability


def test_valid_col_and_value():
    df = pd.read_csv("data/raw/titanic.csv")
    column = "Pclass"
    value = 1
    assert 0 < empirical_probability(df, column, value) < 1


def test_no_value():
    df = pd.DataFrame(
        {"Survived": [1, 0, 1, 0], "Sex": ["male", "female", "female", "male"]}
    )
    column = "Survived"
    value = 4
    assert empirical_probability(df, column, value) == 0.0


def test_no_column():
    df = pd.DataFrame(
        {"Survived": [1, 0, 1, 0], "Sex": ["male", "female", "female", "male"]}
    )
    column = "Age"
    value = 0
    assert empirical_probability(df, column, value) == 0.0


def test_empty_df():
    df = pd.DataFrame()
    column = "Pclass"
    value = 0
    assert empirical_probability(df, column, value) == 0.0
