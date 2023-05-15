#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    x = len(my_list)
    copy_list = my_list.copy()
    if idx < 0:
        return copy_list
    elif idx > n - 1:
        return copy_list
    else:
        copy_list[idx] = element
        return copy_list
