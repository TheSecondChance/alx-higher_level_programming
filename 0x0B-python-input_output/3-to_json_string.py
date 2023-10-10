#!/usr/bin/python3
"""function that returns the JSON representation of an object strin
"""
import json


def to_json_string(my_obj):
    """ JSON representation of an object
        Args:
            my_obj: str representation
        Return: the JSON representation"""

        return json.dumps(my_obj)

