import numpy as np
from src.week2.numpy_basics import (
    array_stats,
    filter_array,
    make_array,
    scale_array,
    slice_array,
)


# ----------- make_array -------------
def test_make_array_returns_ndarray():
    # use isinstance() to check that its the correct type
    result = make_array([1, 2, 3, 4, 5])
    assert isinstance(result, np.ndarray)


def test_make_array_values():
    # checks the values
    result = make_array([10, 20, 30])
    assert list(result) == [10, 20, 30]


def test_make_array_shape():
    # checks the property of the list
    result = make_array([1, 2, 3, 4])
    assert result.shape == (4,)


# ---------- array_stats --------------
def test_array_stats_keys():
    result = array_stats(np.array([1, 2, 3, 4, 5]))
    assert set(result.keys()) == {"mean", "min", "max", "std"}


def test_array_stats_values():
    result = array_stats(np.array([1, 2, 3, 4, 5]))
    assert result["mean"] == 3.0
    assert result["min"] == 1.0
    assert result["max"] == 5.0


def test_array_stats_returns_floats():
    result = array_stats(np.array([1, 2, 3]))
    assert all(isinstance(v, float) for v in result.values())


# ------------- slice_array --------------
def test_slice_array_basic():
    result = slice_array(np.array([10, 20, 30, 40, 50]), 1, 4)
    assert list(result) == [20, 30, 40]


def test_slice_array_from_start():
    result = slice_array(np.array([10, 20, 30, 40, 50]), 0, 3)
    assert list(result) == [10, 20, 30]


def test_slice_array_returns_ndarray():
    result = slice_array(np.array([1, 2, 3, 4, 5]), 0, 2)
    assert isinstance(result, np.ndarray)


# ----------- scale_array ------------------
def test_scale_array_basic():
    result = scale_array(np.array([1, 2, 3, 4, 5]), 2.0)
    assert list(result) == [2.0, 4.0, 6.0, 8.0, 10.0]


def test_scale_array_fraction():
    result = scale_array(np.array([10, 20, 30]), 0.5)
    assert list(result) == [5.0, 10.0, 15.0]


def test_scale_array_returns_ndarray():
    result = scale_array(np.array([1, 2, 3]), 3.0)
    assert isinstance(result, np.ndarray)


# ------------ filter_array ----------------
def test_filter_array_basic():
    result = filter_array(np.array([1, 2, 3, 4, 5]), 3.0)
    assert list(result) == [4, 5]


def test_filter_array_none_pass():
    result = filter_array(np.array([1, 2, 3]), 10.0)
    assert list(result) == []


def test_filter_array_all_pass():
    result = filter_array(np.array([5, 6, 7]), 1.0)
    assert list(result) == [5, 6, 7]


def test_filter_array_returns_ndarray():
    result = filter_array(np.array([1, 2, 3]), 0.0)
    assert isinstance(result, np.ndarray)
