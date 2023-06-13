#!/usr/bin/python3
"""class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        """height and width"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area"""
        return self.__width * self.__height

    def __str__(self):
        ""returns string1"""
        string1 = "[" + str(self.__class__.__name__) + "]"
        string1 += str(self.__width) + "/" + str(self.__height)
        return string1
