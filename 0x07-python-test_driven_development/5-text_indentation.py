#!/usr/bin/python3
"""
This for Module text_indentation
function that prints 2 new lines after "." "?" ":" characters
"""


def text_indentation(text):
    """prints 2 new lines after  "." "?" ":" characters
    Args:
        text (str): input text
    Returns:
        No return
    Raises:
        TypeError: If text is'not a string
    """

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
