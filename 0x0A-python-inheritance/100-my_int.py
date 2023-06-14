#!/usr/bin/python3
"""Defines class MyInt that inherits from int."""


class MyInt(int):
    """MyInt has == and != operators inverted"""

    def __eq__(self, value):
        """overwrites the == with !="""
        return self.real != value

    def __ne__(self, value):
        """overwite != with =="""
        return self.real == value
