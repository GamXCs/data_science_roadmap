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


"""Exercise 2 — Writing a File
pythondef write_lines(filepath: str, lines: list[str]) -> None:
    """Write a list of strings to a file, one per line."""

Use "w" mode
Each line should end with \n"""

def write_lines(filepath: str, lines: list[str]) -> None:
    pass
