from src.week1.analyzer import word_lengths

"""Day 3 - Functions and Modules"""

"""Write a function greet that takes a name and an optional greeting
that defaults to "Hello". It should return a string like "Hello, alice!".
Write a proper docstring inside it."""


def greet(name: str, greeting: str = "Hello") -> str:
    """take a name and return a greeting

    Args:
        name: person's name
        greeting: a greeting, defaults to Hello
    Return:
        A formatted greeting with the person's name
    """
    return f"{greeting}, {name}!"


"""Write a function total that accepts any number of numeric arguments and returns their sum.
It should return 0 if nothing is passed in."""


def total(*args):
    """take any number of args and return their sum. return 0 is nothing is passed in

    Args:
        *args: receive any amount of numbers

    Return:
        0 if nothing is passed and the total sum of numbers if any are provided
    """
    return sum(args)


"""Write a function build_profile that accepts any number of keyword arguments
and returns them as a dict. For example, build_profile(name="alice", age=25)
returns {"name": "alice", "age": 25}"""


def build_profile(**kwargs):
    """Accepts any number of keyword args and returns as a dictionary

    Args:
        **kwargs: anything can be passed into the function call

    Return:
        dictionary with arguments passed
    """
    return kwargs


"""Write a function summarize that takes a required label string,
any number of positional values via
*args, and any number of keyword options via **kwargs.
It should return a dict with three keys: "label", "values"
(the args as a list), and "options" (the kwargs dict)."""


def summarize(label: str, *args, **kwargs):
    """Return a dictionary with 3 keys: label, values, and options

    Args:
        label: label
        *args: any number of positional values
        **kwargs: any number of keyword options

    Return:
        dictionary with 3 keys"""

    return {"label": label, "values": list(args), "options": kwargs}


"""In functions.py, import word_lengths from analyzer.py and write a new function longest_word
that takes a list of words and returns the word with the highest length.
Use word_lengths to do the heavy lifting — don't recompute lengths manually."""


def longest_word(words: list[str]) -> str:
    """return the word with the longest length

    Args:
        words: list of words
    Return:
        word with the longest length
    """
    # import word_lengths function from analyzer.py and store in var
    word = word_lengths(words)

    # return longest word
    return max(word, key=len)


"""Exercise 6 — Default parameters
Write a function format_name(first, last, separator=", ") that returns the name formatted
as "last[separator]first". Test with the default separator and a custom one like " ".
"""


def format_name(first: str, last: str, separator=",") -> str:
    """return formatted name
    Args:
        first: first name
        last: last name
        separator: a comma, but can be altered to a different separator
    Return:
        string in form: last[separator]first
    """
    return f"{last}{separator}{first}"


"""
Exercise 7 — *args
Write a function average(*args) that returns the average of all numbers passed in.
Handle the case where no arguments are passed by returning 0."""


def average(*args):
    """return the average of all numbers passed by - 0 if no args passed
    Args:
        args: any number of positional args
    Return:
        Average of values entered"""
    if not args:
        return 0
    return sum(args) / len(args)


"""
Exercise 8 — **kwargs
Write a function build_query(**kwargs) that takes any number of keyword arguments
and returns a URL query string like "?key1=value1&key2=value2". Order doesn't matter."""


def build_query(**kwargs):
    """func takes any number of keyword args and return a url query string
       ex: ?key1=value1&key2=value2
    Args:
        **kwargs: any number of keyword arguments
    Return:
        a url formatted like "?key1=value1&key2=value2"
    """
    return "?" + "&".join(f"{key}={value}" for key, value in kwargs.items())


"""
Exercise 9 — Combining all three
Write a function log_event(event_type, *args, severity="info", **kwargs) that returns
a formatted string like "[info] click: ('button', 'home') | meta: {'user': 'gamliel'}"."""


def log_event():
    pass


"""
Exercise 10 — Importing between modules
In analyzer.py, write a function shortest_word(words) that returns the shortest word.
Then import and use it in functions.py to write word_length_range(words) that returns a
tuple of (shortest, longest) using both shortest_word and longest_word."""


def shortest_word():
    pass


if __name__ == "__main__":
    pass
