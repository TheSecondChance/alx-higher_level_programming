#!/usr/bin/python3
"""
This for class MyList that inherits from list
"""


class MyList(list):
    """Inherit from list class"""

    def __init__(self):
        """Initialize the object"""
        super().__init__()

    def print_sorted(self):
        """Prints sorted list"""

        new_list = self.copy()
        new_list.sort()
        print("{}".format(new_list))
