#!/usr/bin/python3
# Author: Victor Mwangangi

def max_integer(my_list=[]):
    max_value = 0
    if len(my_list) == 0:
        return None
    else:
        for i in my_list:
            if i > max_value:
                max_value = i
    return max_value
