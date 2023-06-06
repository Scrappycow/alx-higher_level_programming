#!/usr/bin/python3


def max_integer(list=[]):
    """
    prints max integer from a list
    if list is empty returns none
    """
    if len(list) == 0:
        return None
    result = list[0]
    t = 1
    while t < len(list):
        if list[t] > result:
            result = list[t]
        t += 1
    return result
