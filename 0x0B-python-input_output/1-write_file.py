#!/usr/bin/python3
""" Module for task 1 """


def write_file(filename="", text=""):
    """ Function for writing files """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
