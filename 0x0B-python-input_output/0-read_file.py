#!/usr/bin/python3
"""
Defines a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """Read and print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
