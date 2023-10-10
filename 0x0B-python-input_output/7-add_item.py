#!/usr/bin/python3
""" adds all arguments to a Python
    list, and then save them to a file:
"""

import json
import os

from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_item(args, filename):
    """items to a JSON file
        Args:
            args: list items to add.
            filename: path to the JSON file"""

    content = load_from_json(filename) if os.path.exists(filename) else []
    content.extend(args)
    save_to_json(content, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    filename = "add_item.json"
    add_item(args, filename)
