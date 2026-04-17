import numpy as np
import pandas as pd

from src.week2.day3_cleaning import drop_missing_values, fill_missing_values


# ------------- fill_missing_values -----------------
def test_fill_missing_values():
    df = pd.DataFrame({"name": ["Alice", "Bob", None], "age": [25, None, 30]})
    df = fill_missing_values(df, "age", 0)
    assert df["age"].isnull().sum() == 0


def test_fill_missing_values_correct():
    df = pd.DataFrame({"name": ["Alice", "Bob", None], "age": [25, None, 30]})
    df = fill_missing_values(df, "age", 0)
    assert list(df["age"]) == [25.0, 0.0, 30.0]


def test_fill_missing_only_target_column():
    df = pd.DataFrame({"name": ["Alice", "Bob", None], "age": [25, None, 30]})
    df = fill_missing_values(df, "age", 0)
    assert df["name"].isnull().sum() == 1


# ------------- drop_missing_values --------------
def test_drop_missing_values():
    df = pd.DataFrame({"name": ["Alice", "Bob", None], "age": [25, None, 30]})
    df = drop_missing_values(df)
    assert df.isnull().sum().sum() == 0


def test_drop_missing_values_shape():
    df = pd.DataFrame({"name": ["Alice", "Bob", None], "age": [25, None, 30]})
    df = drop_missing_values(df)
    assert df.shape == (1, 2)


def test_drop_missing_values_correct_row():
    df = pd.DataFrame({"name": ["Alice", "Bob", None], "age": [25, None, 30]})
    df = drop_missing_values(df)
    assert list(df["name"]) == ["Alice"]
