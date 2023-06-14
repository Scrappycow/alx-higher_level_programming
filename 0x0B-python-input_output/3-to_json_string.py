#!/usr/bin/python3

"""Module has function that returns JSON rep of an obj"""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object"""

    return json.dumps(my_obj)
