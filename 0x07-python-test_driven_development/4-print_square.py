#!/usr/bin/python3
"""
A module to hold a function that prints a square given a size
"""


def print_square(size):
    """
    Prints a square of hashtags
    Args:
        size: An int to determine the breadth and height of the square
    Returns: Null Void
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size, end="")
        print()
