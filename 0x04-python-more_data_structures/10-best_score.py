#!/usr/bin/python3
# Author: Victor Mwangangi
def best_score(a_dictionary):
    if a_dictionary:
        largest = 0
        largest_key = ""
        for k, v in a_dictionary.items():
            if v >= largest:
                largest = v
                largest_key = k
        return largest_key
    else:
        return None
