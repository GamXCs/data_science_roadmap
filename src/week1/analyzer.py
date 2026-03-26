from collections import Counter, defaultdict

"""Write a function that takes a list of numbers and returns
a new list with only the even numbers, squared. No loops — comprehension only."""


def even_squares(numbers: list[int]) -> list[int]:
    return [num**2 for num in numbers if num % 2 == 0]


print(even_squares([1, 2, 3, 4]))

"""Write a function that takes a list of words and returns a dict mapping each word to its length."""


def word_lengths(words: list[str]) -> dict[str, int]:
    pass


"""Write a function that takes two lists of equal length and returns a list of strings formatted like "1. alice: 92" — pairing an index (1-based), a name, and a score."""


def format_scores(names: list[str], scores: list[int]) -> list[str]:
    pass


"""Exercise 4 — collections.Counter
Write a function that takes a string and returns the 3 most common characters (excluding spaces)."""


def top_charts(text: str, n: int = 3) -> list[tuple[str, int]]:
    pass


"""Exercise 5 — collections.defaultdict
Write a function that takes a list of (student, grade) tuples and returns a dict mapping each student to a list of their grades."""
