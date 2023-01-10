#!/usr/bin/python3
""" Module for task 0 """


def read_file(filename=""):
    """ A function to read a file """
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()
        print(data, end="")
