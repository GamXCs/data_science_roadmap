from analyzer.py import word_lengths

"""Day 3 - Functions and Modules"""

"""Write a function greet that takes a name and an optional greeting
that defaults to "Hello". It should return a string like "Hello, alice!".
Write a proper docstring inside it."""


def greet(name: str, greeting: str = "Hello") -> str:
    """take a name and return a greeting

    Args:
        name: person's name
        greetins: a greeting, defaults to Hello
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


def longest_word():
    pass


if __name__ == "__main__":
    pass
