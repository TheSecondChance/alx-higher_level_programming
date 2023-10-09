#!/usr/bin/python3
"""Module holds a function that determines if an object is an instance of a
class that inherited from a specified class
"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance
    of a class that inherited (directly or indirectly) from the
    specified class otherwise False

    Args:
        obj: this object to check
        a_class: The class to check
    Returns:
        bool: if isinstance othewise false"""

    return True if isinstance(obj, a_class) and \
        type(obj) is not a_class else False
