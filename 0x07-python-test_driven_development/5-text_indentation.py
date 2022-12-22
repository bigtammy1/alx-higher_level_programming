#!/usr/bin/python3
"""
a module to hold a function that
prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Args:
        text: A long string
    Returns:
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    endings = [".", "?", ":"]
    for i in text:
        if i in endings:
            print(f"{i}\n")
        else:
            print(i, end="")
