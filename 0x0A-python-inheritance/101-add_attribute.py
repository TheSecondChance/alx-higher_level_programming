#!/usr/bin/python3
"""Module contains a class that inherits from 'int'
"""


def add_attribute(obj, name, value):
    """Add new attributes if not assigned an
    object if possible.
        Args:
            name (str): the name of the attribute to insert
            value (any): the value of the attribute to insert
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
