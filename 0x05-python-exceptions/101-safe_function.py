#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    try:
        output = fct(*args)
        return (output)
    except Exception as exception:
        print("Exception: {}".format(exception), file=sys.std.err)
