#!/usr/bin/python3
"""
return dict description with simple DS for JSON serialization of an object
"""


def class_to_json(obj):
    """function returns a dict with simple data structure"""

    result = {}
    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()
        return result
