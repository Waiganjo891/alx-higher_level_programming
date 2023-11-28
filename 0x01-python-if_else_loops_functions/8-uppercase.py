#!/usr/bin/python3
def uppercase(str):
    for c in str:
        temp = c
        if ord(temp) >= 97 and ord(temp) <= 122:
            temp = chr(ord(c) - 32)
            print("{}".format(temp), end='')
    print()
