from collections import Counter, defaultdict


# create 3 functions for the CLI
def count_words(text: str) -> Counter:
    """return a frequency counter of words

    Args:
        text: string of words to count
    Return:
        frequency Counter"""
    return Counter(word.strip("!.,?-';:") for word in text.lower())


def top_n_words(counter: Counter, n: int = 10) -> list[tuple[str, int]]:
    """Return the n most common words

    Args:
        counter: Counter
        n: number of top words to compute

    Return:
        n most common words"""
    return counter.most_common(n)


def word_stats(counter: Counter) -> dict:
    "Return total_words, unique_words, most_common, least_common"
    return {
        "total_words": sum(counter.values()),
        "unique_words": len(counter),  # counts all of the keys by default
        "most_common": max(counter.keys(), key=lambda w: counter[w]),
        "least_common": min(counter.keys(), key=lambda w: counter[w]),
    }


# --------------------------------------------------------------------
"""Write a function that takes a list of numbers and returns
a new list with only the even numbers, squared. No loops — comprehension only."""


def even_squares(numbers: list[int]) -> list[int]:
    return [num**2 for num in numbers if num % 2 == 0]


"""Write a function that takes a list of words and returns a dict mapping each word to its length."""


def word_lengths(words: list[str]) -> dict[str, int]:
    return {word: len(word) for word in words}


"""Write a function that takes two lists of equal length and returns a list of strings formatted
like "1. alice: 92" — pairing an index (1-based), a name, and a score."""


def format_scores(names: list[str], scores: list[int]) -> list[str]:
    return [
        f"{index}. {name}: {score}"
        for index, (name, score) in enumerate(zip(names, scores), start=1)
    ]


# test cases
names = ["alice", "bob", "carol"]
scores = [92, 85, 88]
print(format_scores(names, scores))


"""Exercise 4 — collections.Counter
Write a function that takes a string and returns the 3 most common characters (excluding spaces)."""


def top_chars(text: str, n: int = 3) -> list[tuple[str, int]]:
    count = Counter(text.lower().replace(" ", ""))
    return count.most_common(n)


# test cases
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


"""Write a function that takes a list of students and a list of subjects,
and returns a dict where each student maps to a dict of subjects all initialized to 0."""


def grade_template(
    students: list[str], subjects: list[str]
) -> dict[str, dict[str, int]]:
    count = defaultdict(list)
    pass


"""Write a function that takes two lists and returns a list of tuples pairing them up."""


def pair_up(list_a: list, list_b: list) -> list[tuple]:
    return [(a, b) for a, b in zip(list_a, list_b)]


print(pair_up([1, 2, 3], ["a", "b", "c"]))

"""Write a function that takes a list of first names and last names and returns a list of full names as strings."""


def full_names(first_names: list[str], last_names: list[str]) -> list[str]:
    return [f"{first} {last}" for first, last in zip(first_names, last_names)]


print(full_names(["alice", "bob"], ["smith", "jones"]))

"""Write a function that takes a list of items and a list of prices and returns the total cost of all items combined"""


def total_cost(item_list: list[str], price_list: list[float]) -> float:
    # get the prices and sum them
    total = sum(price for item, price in zip(item_list, price_list))
    return total


items = ["apple", "banana", "fig", "grape"]
prices = [1.50, 0.75, 2.00, 3.25]

print(total_cost(items, prices))


"""Write a function that takes a list of strings and returns the most common one."""


def most_common_word(text: list[str]) -> str:
    c = Counter(text)
    return c.most_common(1)[0][0]  # get the first item in the first tuple


print(most_common_word(["apple", "banana", "apple", "fig", "banana", "apple"]))

"""Write a function that takes two strings and returns True if they are anagrams of each other
(contain the same characters in the same quantities), False otherwise. Ignore spaces and case."""


def is_anagram(word1: str, word2: str) -> bool:
    word1_count = Counter(word1.lower().replace(" ", ""))
    word2_count = Counter(word2.lower().replace(" ", ""))

    return word1_count == word2_count


# test cases
print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))
print(is_anagram("Astronomer", "Moon starer"))


"""Write a function that takes a list of words and groups them by their first letter."""


def group_by_letter(words: list[str]) -> dict[str, list[str]]:
    word_dict = defaultdict(list)
    for word in words:
        word_dict[word[0]].append(word)
    return word_dict


"""Write a function that takes a list of (city, temperature) tuples and returns a dict mapping each city to its highest recorded temperature."""


def highest_temp(records: list[tuple[str, float]]) -> dict[str, float]:
    temp_dict = defaultdict(list)

    for city, temps in records:
        temp_dict[city].append(temps)
    return {city: max(temps) for city, temps in temp_dict.items()}


"""Write a function shortest_word that returns the shortest word"""


def shortest_word(words: list[str]) -> str:
    return min(words, key=len)


if __name__ == "__main__":
    print(even_squares([1, 2, 3, 4]))

    print(word_lengths(["bat", "year", "popper", "freedom"]))

    print(group_by_letter(["apple", "banana", "avocado", "blueberry", "cherry"]))

    print(
        highest_temp(
            [
                ("Birmingham", 95),
                ("huntsville", 72),
                ("Birmingham", 88),
                ("huntsville", 80),
            ]
        )
    )

print(count_words("I am I am going to the store"))
