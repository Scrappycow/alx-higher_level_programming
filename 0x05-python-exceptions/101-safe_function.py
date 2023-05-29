#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        output = fct(*args)
        return (output)
    except Exception as exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.std.err)
        return (None)
