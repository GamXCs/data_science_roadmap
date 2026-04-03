from collections import Counter

"""create a function that reads a file"""


def read_lines(filepath: str) -> list[str]:
    """Read a file and return its lines as a list of stripped strings. If
        empty return an empty list

    Args:
        filepath: path of the file of type str
    Return:
        list of stripped strings
    """
    try:
        with open(filepath, mode="r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []


def write_lines(filepath: str, lines: list[str]) -> None:
    """Write a list of strings to a file, one per line.
    Args:
        filepath: filepath
        lines: list of strings
    Return:
        No return, just write to file
    """
    with open(filepath, mode="w") as f:
        for line in lines:
            f.write(line + "\n")


def append_line(filepath: str, line: str) -> None:
    """Append a single line to a file."""
    with open(filepath, mode="a") as f:
        f.write(line + "\n")


"""Case-insensitive (normalize to lowercase)
Strip punctuation from words (hint: str.strip(".,!?"))
Return {} if file not found"""


def word_count(filepath: str) -> dict[str, int]:
    """Return a dict mapping each word to how many times it appears in the file."""
    count = Counter()  # create Counter to store info
    try:
        with open(filepath, mode="r") as f:
            for line in f:  # iterate through lines in file
                words = line.split()  # split words into a list
                for word in words:
                    clean = word.lower().strip(
                        "?!,.-"
                    )  # lowercase & remove punctuation
                    count[clean] += 1  # increase count
    except FileNotFoundError:
        return {}
    return count


# custom error
class EmptyFileError(Exception):
    """Raised when a file exists but contains no content."""

    pass


def read_nonempty(filepath: str) -> list[str]:
    """Read a file; raise EmptyFileError if it's empty, FileNotFoundError if missing."""
    with open(filepath, mode="r") as f:  # read
        lines = [line.strip() for line in f]
        if not lines:  # check if list is empty
            raise EmptyFileError("File is empty")  # raise custom error
        return lines  # return list
