#!/usr/bin/python3
"""Defines a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”"""
    with open(filename) as textfile:
        return json.load(textfile)
