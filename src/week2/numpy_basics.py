import numpy as np

"""Introduction to Numpy:
    Will begin with creating 8 functions"""


def make_array(data: list) -> np.ndarray:
    """take a list and return a numpy array
    Args:
        data: a list
    Return:
        a np array"""
    return np.array(data)


def array_stats(arr: np.ndarray) -> dict:
    """Return a dict with keys "mean", "min", "max", "std"
    Each value should be a float

    Args:
        arr: np.ndarray
    Return:
        dictionary with keys mean, min, max, std"""
    results_dict = {
        "mean": float(arr.mean()),
        "min": float(arr.min()),
        "max": float(arr.max()),
        "std": float(arr.std()),
    }
    return results_dict


def slice_array(arr: np.ndarray, start: int, end: int) -> np.ndarray:
    """Return the slice of arr from start up to (not including) end

    Args:
        arr: np.ndarray
        start: int
        end: int
    Return:
        the slice of the array from start to end (exclusive)"""
    return arr[start:end]


def scale_array(arr: np.ndarray, factor: float) -> np.array:
    """Multiple every element in arr by factor and return the result

    Args:
        arr: np.ndarray
        factor: float
    Return:
        array with every element multiplied by the factor w/o a loop"""

    return arr * factor


def filter_array(arr: np.ndarray, threshold: float) -> np.ndarray:
    """Return only the elements in arr that are greater than threshold
    Do NOT use a loop

    Args:
        arr: np.ndarray
        threshold: float
    Return:
        array with every element thats greater than threshold"""
    return arr[arr > threshold]


if __name__ == "__main__":
    pass
