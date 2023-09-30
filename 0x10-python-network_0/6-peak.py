#!/usr/bin/python3
"""contains the function called find_peak"""


def find_peak(list_of_integers):
    """finds a peak in the list of unsorted integers"""
    li = list_of_integers
    lan = len(li)
    if lan == 0:
        return
    m = lan // 2
    if (m == lan - 1 or li[m] >= li[m + 1]) and (m == 0 or li[m] >= li[m - 1]):
        return li[m]
    if m != l - 1 and li[m + 1] > li[m]:
        return find_peak(li[m + 1:])
    return find_peak(li[:m])
