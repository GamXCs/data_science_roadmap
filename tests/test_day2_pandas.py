import pandas as pd
import pytest
from src.week2.day2_pandas import create_series


def test_create_series_values():
    s = create_series([10, 20, 30], ["a", "b", "c"])
    assert list(s.values) == [10, 20, 30]


def test_create_series_index():
    s = create_series([10, 20, 30], ["a", "b", "c"])
    assert list(s.index) == ["a", "b", "c"]


def test_create_series_length():
    s = create_series([1, 2, 3, 4], ["w", "x", "y", "z"])
    assert len(s) == 4
