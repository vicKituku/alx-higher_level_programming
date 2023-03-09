#!/usr/bin/python3
# Author: Victor Mwangangi
if __name__ == '__main__':
    import sys
    sum = 0
    argument_len = len(sys.argv)
    for index in range(1, argument_len):
        sum += int(sys.argv[index])
    print(sum)
