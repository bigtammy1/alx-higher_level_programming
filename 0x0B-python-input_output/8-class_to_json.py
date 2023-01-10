#!/usr/bin/python3
""" A module for task 8 """


def class_to_json(obj):
    """ A function to convert obj to serializable dict """
    return obj.__dict__
