#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ult = (abs(number) % 10) * -1
else:
    ult = abs(number) % 10

if ult > 5:
    print(f"Last digit of {number} is {ult} and is greater than 5")
elif ult == 0:
    print(f"Last digit of {number} is {ult} and is 0")
elif ult < 6 and not 0:
    print(f"Last digit of {number} is {ult} and is less than 6 and not 0")
