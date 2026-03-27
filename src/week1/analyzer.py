from collections import Counter, defaultdict

"""Write a function that takes a list of numbers and returns
a new list with only the even numbers, squared. No loops — comprehension only."""


def even_squares(numbers: list[int]) -> list[int]:
    return [num**2 for num in numbers if num % 2 == 0]


# test call
print(even_squares([1, 2, 3, 4]))

"""Write a function that takes a list of words and returns a dict mapping each word to its length."""


def word_lengths(words: list[str]) -> dict[str, int]:
    return {word: len(word) for word in words}


print(word_lengths(["bat", "year", "popper", "freedom"]))


"""Write a function that takes two lists of equal length and returns a list of strings formatted
like "1. alice: 92" — pairing an index (1-based), a name, and a score."""


def format_scores(names: list[str], scores: list[int]) -> list[str]:
    return [
        f"{index}. {name}: {score}"
        for index, (name, score) in enumerate(zip(names, scores), start=1)
    ]


names = ["alice", "bob", "carol"]
scores = [92, 85, 88]
print(format_scores(names, scores))


"""Exercise 4 — collections.Counter
Write a function that takes a string and returns the 3 most common characters (excluding spaces)."""


def top_chars(text: str, n: int = 3) -> list[tuple[str, int]]:
    count = Counter(text.lower().replace(" ", ""))
    return count.most_common(n)


print(top_chars("I went to the store", 3))


"""Exercise 5 — collections.defaultdict
Write a function that takes a list of (student, grade) tuples and returns
a dict mapping each student to a list of their grades."""


def group_grades(records: list[tuple[str, int]]) -> dict[str, list[int]]:
    d = defaultdict(list)  # pass the type, not the data

    # loop through records getting name and grade
    for name, grade in records:
        d[name].append(grade)
    return d


print(group_grades([("alice", 90), ("bob", 85), ("alice", 92), ("bob", 88)]))
