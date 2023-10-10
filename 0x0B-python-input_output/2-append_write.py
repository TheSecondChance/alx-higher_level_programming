#!/usr/bin/python3
"""function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file
        Args:
            filename: name of the file
            text: text that write
        Return:
        returns the number of characters added"""

    with open(filename, "a", encoding="utf-8") as file:
        res = file.write(text)
        return res
