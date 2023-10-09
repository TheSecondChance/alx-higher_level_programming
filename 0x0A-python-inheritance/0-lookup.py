#!/usr/bin/python3
""" Module that list of attributes and methods of object"""


def lookup(obj):
    """list of attributes and methods of object
    Args:
        obj(obj) - this for object to check
    Returns:
        list: list attributes and methods
    """

    return dir(obj)
