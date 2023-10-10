#!/usr/bin/python3
"""class Student that defines a studen"""


class Student:
    """create student class"""

    def __init__(self, first_name, last_name, age):
        """
        special method initialize
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrive the dict reprenting"""
        if attrs is None:
            return self.__dict__.copy()
        dicte = {}
        for i in attrs:
            if i in self.__dict.keys():
                dicte[i] = self.__dict__[i]
        return dicte
