#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return (Self.__size) ** 2

    def size(self):

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
        if self.__size == 0:
            print()
            return
        for t in range(self.__size):
            print("".join(["#" for u in range(self.__size)]))
