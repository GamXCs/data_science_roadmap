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


def make_matrix(rows: int, cols: int) -> np.ndarray:
    # Return a 2D array of zeros with the given number of rows and cols
    return np.zeros((rows, cols))


def row_col_stats(matrix: np.ndarray) -> dict:
    # Return a dict with:
    #   "row_means": mean of each row (axis=1)
    #   "col_means": mean of each column (axis=0)
    math_done = {"row_means": matrix.mean(axis=1), "col_means": matrix.mean(axis=0)}
    return math_done


# Real world data science pattern i'll use frequently
# Used to rescale an arr so all values fall between 0-1
# Formula: normalized = (x - min) / (max-min)
def normalize_array(arr: np.ndarray) -> np.ndarray:
    # Apply min-max normalization to arr
    # Result should have min 0.0 and max 1.0
    # Use vectorized operations — no loops
    return (arr - arr.min()) / (arr.max() - arr.min())


if __name__ == "__main__":
    pass
