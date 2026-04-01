from src.week1.functions import (
    average,
    build_profile,
    build_query,
    format_name,
    greet,
    log_event,
    longest_word,
    summarize,
    total,
    word_length_range,
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
    assert build_profile(name="Gam", age=25, city="Birmingham") == {
        "name": "Gam",
        "age": 25,
        "city": "Birmingham",
    }


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


# -------- longest_words ----------
def test_longest_word_empty_dict():
    assert longest_word(["a", "b"]) == "a", "b"


def test_longest_word_with_entries():
    assert longest_word(["test", "hello", "computer", "coding"]) == "computer"


# -------- format_name-----------
def test_regular_formatted_str():
    assert format_name("Gamliel", "Spinoza") == "Spinoza,Gamliel"


def test_spaced_separator():
    assert format_name("Atarah", "Israel", separator=" ") == "Israel Atarah"


# -------- average ----------
def test_five_args_passed():
    assert average(1, 2, 4, 7, 6) == 4


def test_zero_args_passed():
    assert average() == 0


# ----------- build_query ---------
def test_build_query():
    assert build_query(q="python", lang="en", page=1) == "?q=python&lang=en&page=1"


def test_build_query_multiple_args():
    assert (
        build_query(q="java", result="OOP", page=12, paragraph=3)
        == "?q=java&result=OOP&page=12&paragraph=3"
    )


# --------- log_event -----------
def test_log_event_func_base_parameters():
    assert log_event("click", "button") == "[info] click: ('button',) | meta: {}"


def test_w_args():
    assert (
        log_event("click", "button", "home", severity="warning", user="gamliel")
        == "[warning] click: ('button', 'home') | meta: {'user': 'gamliel'}"
    )


# --------- word_length_range -------
def test_word_length():
    assert word_length_range(["at", "bat", "chat"]) == ("at", "chat")


def test_word_length_empty():
    assert word_length_range(["be", "be"]) == ("be", "be")
