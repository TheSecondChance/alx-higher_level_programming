#!/usr/bin/python3
"""Function that write a string to a text file"""


def write_file(filename="", text=""):
    """write a string  to a text fiel
        Args:
            filename: name of the file
            text: write text
        Return:
            the number of characters written"""


    with open(filename, "w", encoding="utf-8") as file:
        res = file.write(text)
        
        return res
