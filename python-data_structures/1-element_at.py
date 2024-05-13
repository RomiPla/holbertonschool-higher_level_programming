#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        retur = None
        if idx > len (my_list) -1:
            retur = None
        else:
            return (idx +1)
