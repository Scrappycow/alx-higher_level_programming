#!/usr/bin/python3
for a in range(97, 123):
    if(char(a) == 'q' or char(a) == 'e'):
        continue
    print("{}".format(chr(a)), end="")
