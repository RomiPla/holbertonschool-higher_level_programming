#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for x in range(0, len(my_list)):
        if my_list[x] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[x])
    return new_list
