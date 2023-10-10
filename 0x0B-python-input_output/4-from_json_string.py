#!/usr/bin/python3
"""function that returns an object Python data structure
represented by a JSON string"""
import json


def from_json_string(my_str):
    """returns an object represented by a JSON string
        Args: my_str json represented string
        Return:  returns an object represented JSON string
    """
    return json.load(my_str)
