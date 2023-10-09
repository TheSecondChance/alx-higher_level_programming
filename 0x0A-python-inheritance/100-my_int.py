#!/usr/bin/python3
"""Moudle a class MyInt inherits from int"""


class MyInt(int):
    """Iveted has == and != operators"""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
