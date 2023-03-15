#!/usr/bin/python3
# Author: Victor Mwangangi
def search_replace(my_list, search, replace):
    return list(map(lambda x: replace if x == search else x, my_list))
