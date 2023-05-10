#!/usr/bin/python3
def fizzbuzz():
    for cat in range(1, 101):
        if (cat % 3 == 0 and cat % 5 == 0):
            print("Fizzbuzz ", end="")
        elif (cat % 3 == 0):
            print("Fizz ", end="")
        elif (cat % 5 == 0):
            print("Buzz ", end="")
        else:
            print("{} ".format(cat), end="")
