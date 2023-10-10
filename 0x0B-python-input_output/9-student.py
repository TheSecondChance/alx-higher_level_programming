#!/usr/bin/python3
"""class Student that defines a studen"""


class Student:
    """create student class"""

    def __init__(self, first_name, last_name, age):
        """
        special method initialize
        """
        self.name = first_name
        self.lname = last_name
        self.age = age

    def to_json(self):
        """Retrive the dict reprenting"""
        return self.__dict__.copy()
