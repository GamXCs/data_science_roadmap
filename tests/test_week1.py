# tests/test_week1.py

from src.week1.analyzer import (
    even_squares,
    format_scores,
    full_names,
    group_by_letter,
    group_grades,
    highest_temp,
    is_anagram,
    most_common_word,
    pair_up,
    top_chars,
    total_cost,
    word_lengths,
)

# --- even_squares ---


def test_even_squares_returns_only_evens_squared():
    assert even_squares([1, 2, 3, 4]) == [4, 16]


def test_even_squares_with_all_odd_numbers():
    assert even_squares([1, 3, 5]) == []


def test_even_squares_with_empty_list():
    assert even_squares([]) == []


# --- word_lengths ---


def test_word_lengths_maps_words_to_their_length():
    assert word_lengths(["bat", "year"]) == {"bat": 3, "year": 4}


def test_word_lengths_with_empty_list():
    assert word_lengths([]) == {}


# --- format_scores ---


def test_format_scores_produces_correct_format():
    result = format_scores(["alice", "bob"], [92, 85])
    assert result == ["1. alice: 92", "2. bob: 85"]


def test_format_scores_index_starts_at_one():
    result = format_scores(["carol"], [88])
    assert result[0].startswith("1.")


# --- top_chars ---


def test_top_chars_returns_three_most_common():
    result = top_chars("aabbcc", 3)
    chars = [char for char, count in result]
    assert set(chars) == {"a", "b", "c"}


def test_top_chars_excludes_spaces():
    result = top_chars("a a a", 1)
    assert result[0][0] == "a"


def test_top_chars_is_case_insensitive():
    result = top_chars("AAAaaa", 1)
    assert result[0] == ("a", 6)


# --- group_grades ---


def test_group_grades_collects_all_grades_per_student():
    records = [("alice", 90), ("bob", 85), ("alice", 92)]
    result = group_grades(records)
    assert result["alice"] == [90, 92]
    assert result["bob"] == [85]


def test_group_grades_with_single_record():
    result = group_grades([("alice", 90)])
    assert result["alice"] == [90]


# --- pair_up ---


def test_pair_up_zips_two_lists_into_tuples():
    assert pair_up([1, 2], ["a", "b"]) == [(1, "a"), (2, "b")]


def test_pair_up_with_empty_lists():
    assert pair_up([], []) == []


# --- full_names ---


def test_full_names_joins_first_and_last():
    result = full_names(["alice", "bob"], ["smith", "jones"])
    assert result == ["alice smith", "bob jones"]


# --- total_cost ---


def test_total_cost_sums_all_prices():
    result = total_cost(["apple", "banana"], [1.50, 0.75])
    assert result == 2.25


def test_total_cost_with_single_item():
    assert total_cost(["fig"], [2.00]) == 2.00


# --- most_common_word ---


def test_most_common_word_returns_the_top_word():
    words = ["apple", "banana", "apple", "fig", "apple"]
    assert most_common_word(words) == "apple"


def test_most_common_word_with_single_word():
    assert most_common_word(["banana"]) == "banana"


# --- is_anagram ---


def test_is_anagram_returns_true_for_anagrams():
    assert is_anagram("listen", "silent") is True


def test_is_anagram_returns_false_for_non_anagrams():
    assert is_anagram("hello", "world") is False


def test_is_anagram_ignores_spaces_and_case():
    assert is_anagram("Astronomer", "Moon starer") is True


# --- group_by_letter ---


def test_group_by_letter_groups_correctly():
    result = group_by_letter(["apple", "avocado", "banana"])
    assert result["a"] == ["apple", "avocado"]
    assert result["b"] == ["banana"]


def test_group_by_letter_with_single_word():
    result = group_by_letter(["cherry"])
    assert result["c"] == ["cherry"]


# --- highest_temp ---


def test_highest_temp_returns_max_per_city():
    records = [("Birmingham", 95), ("Birmingham", 88), ("huntsville", 80)]
    result = highest_temp(records)
    assert result["Birmingham"] == 95
    assert result["huntsville"] == 80


def test_highest_temp_with_single_record():
    result = highest_temp([("Mobile", 90)])
    assert result["Mobile"] == 90
