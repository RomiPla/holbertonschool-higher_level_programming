#!/usr/bin/python3
def safe_print_division(x, y):
    global result
    result = 0
    try:
        result = x / y
    except (ValueError, TypeError, IndexError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
