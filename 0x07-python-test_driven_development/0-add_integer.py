#!/usr/bin/python3

"""
0-add_integer module
"""


def add_integer(a, b=98):
    """
    return the sum of integers a and b.
    a and b must be floats or ints else TypeError
    a and b must be type casted to ints.
    returns an int (sum of a and b)
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
