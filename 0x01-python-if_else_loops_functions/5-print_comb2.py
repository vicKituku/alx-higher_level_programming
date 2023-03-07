#!/usr/bin/python3
for num in range(100):
    if num < 10:
        num = "0{}".format(str(num))
    if num != 99:
        print("{}, ".format(num), end='')
    else:
        print("{}".format(num))
