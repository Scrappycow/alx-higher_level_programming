#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    total = 0
    for t in range(len(sys.arg) - 1):
        total += int(sys.arg[t + 1])
    print("{}".format(total))
