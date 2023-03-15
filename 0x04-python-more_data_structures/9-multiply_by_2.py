#!/usr/bin/python3
# Author: Victor Mwangangi
def multiply_by_2(a_dictionary):
    a_dictionary_new = a_dictionary.copy()
    for k in a_dictionary.keys():
        a_dictionary_new[k] *= 2
    return a_dictionary_new
