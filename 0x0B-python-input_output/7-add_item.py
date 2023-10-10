#!/usr/bin/python3
"""adds all arguments to a Python list, and save them to a file
"""
import sys
import os
save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file


def add_item(args, filename):
    """Adds items JSON file.
    Args:
        args: list of items to add.
        filename: path to the JSON file.
    """
    content = load_from_json(filename) if os.path.exists(filename) else []
    content.extend(args)
    save_to_json(content, filename)

if __name__ == "__main__":
    args = sys.argv[1:]
    filename = "add_item.json"
    add_item(args, filename)
