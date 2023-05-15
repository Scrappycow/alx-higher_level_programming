#!/usr/bin/python3

def no_c(my_string):
    remove_c = [y for y in my_string if y != 'c' and y != 'C']
    return ("".join(remove_c))
