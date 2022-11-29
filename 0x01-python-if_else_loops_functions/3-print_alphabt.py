#!/usr/bin/python3
number = 97
while number <= 122:
    if number != ord('q') and number != ord('e'):
        print("{}".format(chr(number)), end="")
    number += 1
