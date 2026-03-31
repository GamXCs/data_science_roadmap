from src.week1.functions import (
    build_profile,
    greet,
    summarize,
    total,
)

"""function tests"""


# -------- greet ----------
def test_greet_no_parameter_given():
    assert greet("Gam") == "Hello, Gam!"


def test_greet_uses_custom_greeting():
    assert greet("alice", greeting="Wassup") == "Wassup, alice!"


# -------- total ------------
def test_total_with_no_args():
    assert total() == 0


def test_total_with_values():
    assert total(2, 3, 5, 7) == 17


# ------- build_profile --------
def test_build_profile_with_standard():
    assert build_profile(name="Gam", age=25) == {"name": "Gam", "age": 25}


def test_build_profile_with_no_kwargs():
    assert build_profile() == {}


# -------- summarize -----------
def test_summarize_with_args():
    assert summarize("grades", 89, 99, 76, 100, subject="math", semester="spring") == {
        "label": "grades",
        "values": [89, 99, 76, 100],
        "options": {"subject": "math", "semester": "spring"},
    }


def test_summarize_empty_args():
    assert summarize("empty") == {"label": "empty", "values": [], "options": {}}
