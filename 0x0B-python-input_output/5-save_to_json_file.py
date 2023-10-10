#!/usr/bin/python3
"""function that writes an Object to a text file
using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """JSON representation
        Args:
            my_obj: object to a text fiel
            filename: the name of file
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
