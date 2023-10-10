#!/usr/bin/python3
"""function that read a text file"""


def read_file(filename=""):
    """print file in to stdout
        Args:
            filename: name of the file inputed
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
