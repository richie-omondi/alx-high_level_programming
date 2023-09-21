#!/usr/bin/python3
"""
Module that returns True if the object is exactly an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Function that returns True if the object is exactly an instance of the specified class ; otherwise False.

    Args:
        obj (obj): object 1
        a_class (class): specified class

    Returns:
        bool: if same True else False
    """

    return type(obj) is a_class
