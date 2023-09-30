#!/usr/bin/python3
"""
The Module is 3-say_my_name
This module function that prints out the given args
"""


def say_my_name(first_name, last_name=""):
    """
    Function that first and last
    Args:
        first_name (str): A string passed as the first args
        last_name (str): A string passed as second args
    Returns:
        string "first_name + last_name"
    Raises:
        TypeError: if any of the args are not of string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

