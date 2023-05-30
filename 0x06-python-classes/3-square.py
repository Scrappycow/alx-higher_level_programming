#!/usr/bin/python3
"""define a class Square"""


class Square:
    """represent a square"""

    def __init__(self, size=0):
        """Initialize a square

        Args:
        size (int): new square size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        return (self.__size) ** 2
