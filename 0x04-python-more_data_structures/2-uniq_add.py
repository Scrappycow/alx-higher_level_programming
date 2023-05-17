#!/usr/bin/python3

def uniq_add(my_list=[]):
    newest_list = set(my_list)
    result = 0
    for t in newest_list:
        result += t
        return (result)
