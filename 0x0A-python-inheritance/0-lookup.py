#!/usr/bin/python3
"""Defines a function that returns the list of
available attributes and methods of an object"""


def lookup(obj):
    """returns a list of attrributes and
    methods of the passed object"""
    return dir(obj)
