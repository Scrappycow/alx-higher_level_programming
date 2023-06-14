#!/usr/bin/python3
"""Class student"""


class Student:
    """class Student with attributes name and age"""

    def __init__(self, first_name, last_name, age):
        """initialize a class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return self.__dict__.copy()
