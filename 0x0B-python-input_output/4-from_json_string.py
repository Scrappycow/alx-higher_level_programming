#!/usr/bin/python3
"""Module returns an object rep by a JSON string"""
import json


def from_json_string(my_str):
    """function returns an object by a JSON string"""
    return json.loads(my_str)
