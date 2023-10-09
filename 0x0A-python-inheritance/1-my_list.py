#!/usr/bin/python3
"""This for class MyList inherits from list"""


class MyList(list):
    """Inherit from list class"""

    def __init__(self):
        """Initialize the object"""

        super().__init__()

    def print_sorted(self):
        """Print sorted lsit"""

        print(sorted(self))
