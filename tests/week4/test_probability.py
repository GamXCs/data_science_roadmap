import pandas as pd
import pytest

from src.week4.probability import (
    bayes_theorem,
    conditional_probability,
    empirical_probability,
    expected_value,
    probability_distribution,
)


def test_valid_col_and_value():
    df = pd.read_csv("data/raw/titanic.csv")
    column = "Pclass"
    value = 1
    assert 0 < empirical_probability(df, column, value) < 1


def test_no_value():
    df = pd.DataFrame(
        {"Survived": [1, 0, 1, 0], "Sex": ["male", "female", "female", "male"]}
    )
    column = "Survived"
    value = 4
    assert empirical_probability(df, column, value) == 0.0


def test_no_column():
    df = pd.DataFrame(
        {"Survived": [1, 0, 1, 0], "Sex": ["male", "female", "female", "male"]}
    )
    column = "Age"
    value = 0
    assert empirical_probability(df, column, value) == 0.0


def test_empty_df():
    df = pd.DataFrame()
    column = "Pclass"
    value = 0
    assert empirical_probability(df, column, value) == 0.0


# test cases for conditional_probability()
def test_valid_case_females():
    df = pd.read_csv("data/raw/titanic.csv")
    assert conditional_probability(df, "Survived", 1, "Sex", "female") >= 0.7


def test_valid_case_males():
    df = pd.read_csv("data/raw/titanic.csv")
    assert conditional_probability(df, "Survived", 1, "Sex", "male") <= 0.3


def test_col_not_exist():
    df = pd.DataFrame(
        {"Survived": [1, 0, 1, 0], "Sex": ["male", "female", "female", "male"]}
    )
    assert conditional_probability(df, "Pclass", 1, "Sex", "male") == 0.0


def test_no_rows_match():
    pass


# test cases for bayes function
# See if the bayes theorem is the same as the results from
# conditional probability function
def test_bayes():
    df = pd.read_csv("data/raw/titanic.csv")
    p_a = empirical_probability(df, "Survived", 1)
    p_b_given_a = conditional_probability(df, "Sex", "female", "Survived", 1)
    p_b = empirical_probability(df, "Sex", "female")
    assert bayes_theorem(p_a, p_b_given_a, p_b) == conditional_probability(
        df, "Survived", 1, "Sex", "female"
    )


def test_expected_value_coin_flip():
    assert expected_value([10, 0], [0.5, 0.5]) == 5.0


def test_expected_value_fair_die():
    result = expected_value([1, 2, 3, 4, 5, 6], [1 / 6] * 6)
    assert abs(result - 3.5) < 1e-9


def test_expected_value_mismatched_lengths():
    assert expected_value([1, 2, 3], [0.5, 0.5]) == 0.0


def test_expected_value_empty_lists():
    assert expected_value([], []) == 0.0


def test_distribution_sums_to_one():
    df = pd.read_csv("data/raw/titanic.csv")
    dist = probability_distribution(df, "Pclass")
    assert abs(sum(dist.values()) - 1.0) < 1e-9


def test_distribution_known_values():
    df = pd.DataFrame({"color": ["red", "red", "blue", "red"]})
    dist = probability_distribution(df, "color")
    assert dist["red"] == 0.75
    assert dist["blue"] == 0.25


def test_distribution_missing_column():
    df = pd.DataFrame({"a": [1, 2]})
    assert probability_distribution(df, "nope") == {}


def test_distribution_empty_df():
    df = pd.DataFrame({"a": []})
    assert probability_distribution(df, "a") == {}
