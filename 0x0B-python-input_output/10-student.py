#!/usr/bin/python3
"""Class student"""


class Student:
    """class Student with attributes name and age"""

    def __init__(self, first_name, last_name, age):
        """initialize a class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        obj = self.__dict__.copy()
        if type(attrs) is list:
            for item in attrs:
                if type(item) is not str:
                    return obj

            dict_list = {}

            for cats in range(len(attrs)):
                for cat in obj:
                    if attrs[cats] == cat:
                        new_list[cat] = obj[cat]
            return dict_list

        return obj
