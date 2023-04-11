#!/usr/bin/python3
"""Defines  a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square."""
    def __init__(self, size):
        """Initialize a new Square instance."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
