#!/usr/bin/python3
"""
Module Name: 0-add_integer
Holds function for Task 0: a function that adds 2 integers.
Project: 0x07 Python Test Driven Development
"""


def add_integer(a, b=98):
    """ Args: a: int or float b: int or float
    Returns: (int) The sum of a and b
    """
    if a is None or not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    else:
        a = int(a)
    if b is None or not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    else:
        b = int(b)

    return a + b
