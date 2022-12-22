#!/usr/bin/python3
"""
A module containing a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Prints first_name and last_name in a string
    Args:
        first_name: a string holding the first name
        last_name: a string holding the last name

    Returns: Null void
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
