#!/usr/bin/python3
# Author: Victor Mwangangi
if __name__ == '__main__':
    import sys
arguments = len(sys.argv)
if arguments == 1:
    print("0 arguments.")
elif arguments == 2:
    print("{} argument:".format(arguments-1))
    print("1: {}".format(sys.argv[1]))
else:
    print("{} arguments:".format(arguments-1))
    for index in range(arguments-1):
        print("{}: {}".format(index+1, sys.argv[index+1]))
