#!/usr/bin/python3
"""
adds a new attribute to an object if it’s possible
"""

def add_attribute(obj, attribute, value):
    """adds a new attribute to an object if it’s possible"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add a new attribute")
    setattr(obj, attribute, value)
