#!/usr/bin/python3
"""appends string at the end of a text file and returns num of chars added"""


def append_write(filename="", text=""):
    """appends string at the end of a file and returns num of chars added"""
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
