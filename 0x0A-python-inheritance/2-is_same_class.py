#!/usr/bin/python3
"""Module has a functction that checks if an object is an instance
or specified class"""


def is_same_class(obj, a_class):
    """ returns True if the object is exactly an
        instance of the specified class otherwise False
    Args:
        obj: this for object to check
        a_class: The class to check against
    Returns:
        bool: True if the object is an instanc othewise false"""

    return True if type(obj) is a_class else False
