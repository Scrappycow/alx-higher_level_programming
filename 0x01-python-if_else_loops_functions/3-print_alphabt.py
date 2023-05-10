#!/usr/bin/python3
for a in range(97, 123):
    if(a == 'q' or a == 'e'):
        continue
    print("{}".format(chr(a)), end="")
