import pandas as pd
import pytest
from src.week2.day2_pandas import (
    add_column,
    create_dataframe,
    create_series,
    drop_column,
    filter_rows,
    select_column,
    select_row_by_label,
    select_row_by_position,
)


# ---------- create_series -------------------
def test_create_series_values():
    s = create_series([10, 20, 30], ["a", "b", "c"])
    assert list(s.values) == [10, 20, 30]


def test_create_series_index():
    s = create_series([10, 20, 30], ["a", "b", "c"])
    assert list(s.index) == ["a", "b", "c"]


def test_create_series_length():
    s = create_series([1, 2, 3, 4], ["w", "x", "y", "z"])
    assert len(s) == 4


# ----------- create_dataframe --------------
def test_dataframe_columns():
    df = create_dataframe({"name": ["Alice", "Bob"], "age": [25, 30]})
    assert list(df.columns) == ["name", "age"]


def test_dataframe_shape():
    df = create_dataframe({"name": ["Alice", "Bob"], "age": [25, 30]})
    assert df.shape == (2, 2)


def test_dataframe_values():
    df = create_dataframe({"x": [1, 2, 3], "y": [4, 5, 6]})
    assert list(df["x"]) == [1, 2, 3]


def test_select_column():
    df = create_dataframe({"name": ["Alice", "Bob"], "age": [25, 30]})
    assert list(select_column(df, "name")) == ["Alice", "Bob"]


def test_select_row_by_label():
    df = create_dataframe({"name": ["Alice", "Bob"], "age": [25, 30]})
    row = select_row_by_label(df, 0)
    assert row["name"] == "Alice"


def test_select_row_by_position():
    df = create_dataframe({"name": ["Alice", "Bob"], "age": [25, 30]})
    row = select_row_by_position(df, 1)
    assert row["name"] == "Bob"


# ----------- filter_rows -------------------
def test_filter_rows_returns_correct_rows():
    df = create_dataframe({"name": ["Alice", "Bob", "Carol"], "age": [25, 30, 25]})
    result = filter_rows(df, "age", 25)
    assert list(result["name"]) == ["Alice", "Carol"]


def test_filter_rows_shape():
    df = create_dataframe({"name": ["Alice", "Bob", "Carol"], "age": [25, 30, 25]})
    result = filter_rows(df, "age", 25)
    assert result.shape == (2, 2)


def test_filter_rows_no_match():
    df = create_dataframe({"name": ["Alice", "Bob"], "age": [25, 30]})
    result = filter_rows(df, "age", 99)
    assert len(result) == 0


# ------------ drop/add_column --------------
def test_add_column():
    df = create_dataframe({"name": ["Alice", "Bob"], "age": [25, 30]})
    df = add_column(df, "city", ["Birmingham", "Houston"])
    assert "city" in df.columns
    assert list(df["city"]) == ["Birmingham", "Houston"]


def test_drop_column():
    df = create_dataframe({"name": ["Alice", "Bob"], "age": [25, 30]})
    df = drop_column(df, "age")
    assert "age" not in df.columns


def test_drop_column_shape():
    df = create_dataframe({"name": ["Alice", "Bob"], "age": [25, 30]})
    df = drop_column(df, "age")
    assert df.shape == (2, 1)
