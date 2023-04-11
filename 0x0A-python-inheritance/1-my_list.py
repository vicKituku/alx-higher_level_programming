#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""


class Mylist(list):
    """Provides a custom implementation of sorted printing
    functionality for the built-in list class"""

    def print_sorted(self):
        """print the passed list in ascending order"""
        print(sorted(self))
