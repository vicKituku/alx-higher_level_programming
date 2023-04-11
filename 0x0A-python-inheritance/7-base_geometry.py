#!/usr/bin/python3
"""Defines a class called BaseGeometry"""


class BaseGeometry:
    """Represents BaseGeometry"""

    def area(self):
        """Raises:
            Exception: This method is not implemented in this base class."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
