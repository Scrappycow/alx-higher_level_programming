#!/usr/bin/python3

def inherits_from(obj, a_class):
    """object - instance of a class that inherited from the specified class"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
