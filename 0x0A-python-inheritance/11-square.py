#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""class Rectangle"""


class Square(Rectangle):
    """class Rectangle"""

    def __init__(self, size):
        """integer validator"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
