#!/usr/bin/python3
# Author: Victor Mwangangi
def uniq_add(my_list=[]):
    res = 0
    for num in set(my_list):
        res += num
    return res
