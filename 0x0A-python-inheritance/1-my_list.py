#!/usr/bin/python3
"""
class MyList that inherits from list Class
"""


class MyList(list):

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
