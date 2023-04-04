#!/usr/bin/python3
"""
Prints the string "My name is <first_name> <last_name>"
raises TypeError: if first_name or last_name are not strings
"""
def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
