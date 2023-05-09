#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number1 = str(number)
number1 = number1[-1]
if number1 > str(5):
    print(f"Last digit of {number} is {number1} and is greater than 5")
elif number1 == str(0):
    print(f"Last digit of {number} is {number1} and is 0")
else:
    print(f"Last digit of {number} is {number1} and is less than 6 and not 0")
