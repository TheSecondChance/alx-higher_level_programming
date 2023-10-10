#!/usr/bin/python3
"""text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename, encoding="utf8") as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, mode="w") as file:
        file.write(text)
