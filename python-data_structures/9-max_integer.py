#!/usr/bin/python3
def max_integer(my_list=[]):
    if (my_list is None) or (len(my_list) <= 0):
        return
    maxint = my_list[0]
    for x in my_list:
        if (maxint < x):
            maxint = x
    return maxint
