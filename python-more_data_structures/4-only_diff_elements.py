#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    for x in set_1:
        if x not in set_2:
            new_set.append(x)
    for y in set_2:
        if y not in set_1:
            new_set.append(y)
    return new_set