#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if x % 15 == 0:
            x = "FizzBuzz"
        elif x % 3 == 0:
            x = "Fizz"
        elif x % 5 == 0:
            x = "Buzz"
        else:
            x = x
        print("{} ".format(x), end='')
