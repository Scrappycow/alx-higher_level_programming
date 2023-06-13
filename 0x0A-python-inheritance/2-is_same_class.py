#!/usr/bin/python3

def is_same_class(obj, a_class):
    """True = the object is exactly an instance of specified class"""

    if type(obj) == a_class:
        return True
    return False
