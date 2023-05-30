#!/usr/bin/python3
"""define a new class Square"""


class Square:
    """a new square"""

    def __init__(self, size=0):
        """initialize a new square

        Args:
        size (int): new square size
        """
        self.size = size

    def area(self):
        """return area of the current square"""
        return (Self.__size) ** 2

    def size(self):
        """set size of current square"""
        return self.__size

    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
