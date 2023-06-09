#!/usr/bin/python3

"""reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """prints file in UTF8"""
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
