import numpy as np

from src.week2.numpy_basics import make_array


# ----------- make_array -------------
def test_make_array_returns_ndarray():
    result = make_array([1, 2, 3, 4, 5])
    assert isinstance(result, np.ndarray)


def test_make_array_values():
    result = make_array([10, 20, 30])
    assert list(result) == [10, 20, 30]


def test_make_array_shape():
    result = make_array([1, 2, 3, 4])
    assert result.shape == (4,)
