#!/usr/bin/python3
""" Module for task 13 """


def append_after(filename="", search_string="", new_string=""):
    """ Finds a search string and adds a new string after it """
    lines = []
    with open(filename, "r") as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w') as f:
        f.writelines(lines)
