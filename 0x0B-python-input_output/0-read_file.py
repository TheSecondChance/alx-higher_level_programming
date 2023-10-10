#!/usr/bin/python3
"""function that read a text file"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        content = file.read()
        print(content)
