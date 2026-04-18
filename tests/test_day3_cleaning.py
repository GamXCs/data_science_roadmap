import numpy as np
import pandas as pd

from src.week2.day3_cleaning import (
    change_dtype,
    drop_duplicates,
    drop_missing_values,
    fill_missing_values,
    rename_columns,
    strip_whitespace,
)


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


# ----------- drop_duplicates --------------
def test_drop_duplicates():
    df = pd.DataFrame({"name": ["Alice", "Bob", "Alice"], "age": [25, 30, 25]})
    df = drop_duplicates(df)
    assert df.shape == (2, 2)


def test_drop_duplicates_correct_rows():
    df = pd.DataFrame({"name": ["Alice", "Bob", "Alice"], "age": [25, 30, 25]})
    df = drop_duplicates(df)
    assert list(df["name"]) == ["Alice", "Bob"]


def test_drop_duplicates_no_duplicates():
    df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})
    df = drop_duplicates(df)
    assert df.shape == (2, 2)


# ------------ rename_columns ---------------
def test_rename_columns():
    df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})
    df = rename_columns(df, {"name": "full_name", "age": "years"})
    assert list(df.columns) == ["full_name", "years"]


def test_rename_single_column():
    df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})
    df = rename_columns(df, {"name": "full_name"})
    assert "full_name" in df.columns
    assert "age" in df.columns


def test_rename_preserves_values():
    df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})
    df = rename_columns(df, {"name": "full_name"})
    assert list(df["full_name"]) == ["Alice", "Bob"]


# --------------- change_dtype -----------------
def test_change_dtype_to_float():
    df = pd.DataFrame({"age": ["25", "30", "35"]})
    df = change_dtype(df, "age", float)
    assert df["age"].dtype == float


def test_change_dtype_to_int():
    df = pd.DataFrame({"score": [88.5, 92.0, 79.0]})
    df = change_dtype(df, "score", int)
    assert df["score"].dtype == int


def test_change_dtype_to_string():
    df = pd.DataFrame({"age": [25, 30, 35]})
    df = change_dtype(df, "age", str)
    assert df["age"].dtype == object


# ---------- strip_whitespace ---------------
def test_strip_whitespace():
    df = pd.DataFrame({"name": ["  Alice", "Bob  ", "  Carol  "]})
    df = strip_whitespace(df, "name")
    assert list(df["name"]) == ["Alice", "Bob", "Carol"]


def test_strip_whitespace_no_change():
    df = pd.DataFrame({"name": ["Alice", "Bob", "Carol"]})
    df = strip_whitespace(df, "name")
    assert list(df["name"]) == ["Alice", "Bob", "Carol"]


def test_strip_whitespace_preserves_other_columns():
    df = pd.DataFrame({"name": ["  Alice  "], "age": [25]})
    df = strip_whitespace(df, "name")
    assert list(df["age"]) == [25]
