#!/usr/bin/python3
# Author: Victor Mwangangi

def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for num in my_list:
            print("{:d}".format(num))
