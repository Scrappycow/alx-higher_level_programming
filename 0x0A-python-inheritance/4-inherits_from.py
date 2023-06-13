#!/usr/bin/python3
"""
object - instance of a class that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """object - instance of a class that inherited from the specified class"""

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
