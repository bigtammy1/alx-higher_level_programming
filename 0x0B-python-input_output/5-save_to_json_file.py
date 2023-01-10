#!/usr/bin/python3
""" Module for task 5 """
import json


def save_to_json_file(my_obj, filename):
    """ Function that saves json to file """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
