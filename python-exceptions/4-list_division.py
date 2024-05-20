#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = []
    for x in range(list_length):
        y = 0
        try:
            y = my_list_1[x] / my_list_2[x]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            i.append(y)
    return i
