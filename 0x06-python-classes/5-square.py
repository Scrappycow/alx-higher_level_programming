#!/usr/bin/python3
"""define a class Square"""


class Square:
    """Rep aa square"""

    def __init__(self, size=0):
        """create a new square

        Args:
        size (int): size of new square
        """
        self.size = size

    def area(self):
        """return are of current square"""
        return (Self.__size) ** 2

    def size(self):
        """set the size of the currebr square"""
        return self.__size

    def soze(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """print the square using # character"""
        if self.__size == 0:
            print()
            return
        for t in range(self.__size):
            print("".join(["#" for u in range(self.__size)]))
