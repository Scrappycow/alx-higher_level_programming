#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """True, if an object is an instance inherited from the specified class"""

    if isinstance(obj, a_class):
        return True
    return False