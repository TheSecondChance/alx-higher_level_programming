#!/usr/bin/python3

"""Module checks if an object is an instance of class or inherited class
"""


def is_kind_of_class(obj, a_class):
    """Function that returns True if the object is an instance of
    or if the object is an instance of a class that inherited from
    the specified class ; otherwise False
    Args:
        obj: this for object to check
        a_class: The class to check against
    Returns:
        bool: if isinstance othewise false"""

    return True if isinstance(obj, a_class) else False
