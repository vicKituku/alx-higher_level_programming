#!/usr/bin/python3
# Author: Victor Mwangangi
def print_sorted_dictionary(a_dictionary):
    for k in sorted(a_dictionary):
        print(f"{k}: {a_dictionary[k]}")
