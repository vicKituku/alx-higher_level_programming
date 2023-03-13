#!/usr/bin/python3
# Author: Victor Mwangangi
def no_c(my_string):
    new_list = []
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        new_list.append(char)
    new_string = "".join(new_list)
    return new_string
