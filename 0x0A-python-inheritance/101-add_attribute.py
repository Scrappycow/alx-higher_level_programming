#!/usr/bin/python3
"""add attribute module"""


def add_attribute(obj, attribute, value):
    """adds a new attribute to an object if it’s possible"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add a new attribute")
    if (not hasattr(obj, attribute)):
        obj.__setattr__(attribute, value)
