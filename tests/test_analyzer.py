from collections import Counter

from src.week1.analyzer import count_words, top_n_words, word_stats


# ------------ count_words ------------------
def test_correct_word_count_strip():
    # check if the strip() method works
    text = "the cat sat()@ on !the mat the"
    assert count_words(text) == {"the": 3, "cat": 1, "sat": 1, "on": 1, "mat": 1}


# ------------ top_n_words ------------------
def test_top_n_words_default_n():
    # When there are fewer words than n, return all of them
    counter = Counter({"the": 5, "cat": 3})
    assert top_n_words(counter) == [("the", 5), ("cat", 3)]


def test_top_n_words_ordering():
    # Results must come back highest-count first
    counter = Counter({"a": 1, "b": 3, "c": 2})
    assert top_n_words(counter, n=3) == [("b", 3), ("c", 2), ("a", 1)]


# ------------ word_stats ------------------
def test_word_stats():
    counter = Counter({"the": 5, "cat": 3, "sat": 1})
    result = word_stats(counter)
    assert result["total_words"] == 9
    assert result["unique_words"] == 3
    assert result["most_common"] == "the"
    assert result["least_common"] == "sat"


# count_words — check that a simple string returns the right counts
# top_n_words — check it returns the right length and the most frequent word is first
# word_stats — check all four keys come back with the right values
