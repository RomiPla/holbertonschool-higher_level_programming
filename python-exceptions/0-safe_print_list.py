#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for y in range(x):
            print("{}".format(my_list[y]), end='')
    except IndexError:
        return y
    else:
        return x
    finally:
        print("")
