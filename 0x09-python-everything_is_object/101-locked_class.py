#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    Prevents the user from instantiating new attributes other than ones named 'first_name
    """

    __slots__ = ["first_name"]
