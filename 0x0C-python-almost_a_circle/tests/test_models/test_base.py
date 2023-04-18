#!/usr/bin/python3
"""
Unit tests for base.py
"""

import unittest
import os
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def test_id(self):
        """Test assigning and incrementing of id attribute"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        """Test conversion of dictionary to json string"""
        r1 = {"id": 1, "width": 5, "height": 10, "x": 2, "y": 3}
        r2 = {"id": 2, "width": 10, "height": 15, "x": 0, "y": 0}
        json_string = Base.to_json_string([r1, r2])
        self.assertEqual(json_string, '[{"id": 1, "width": 5, "height": 10, "x": 2, "y": 3}, '
                                       '{"id": 2, "width": 10, "height": 15, "x": 0, "y": 0}]')
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_save_to_file(self):
        """Test saving of json string to file"""
        r1 = {"id": 1, "width": 5, "height": 10, "x": 2, "y": 3}
        r2 = {"id": 2, "width": 10, "height": 15, "x": 0, "y": 0}
        Base.save_to_file([Base(**r1), Base(**r2)])
        with open("Base.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1, "width": 5, "height": 10, "x": 2, "y": 3}, '
                                       '{"id": 2, "width": 10, "height": 15, "x": 0, "y": 0}]')
        os.remove("Base.json")

    def test_from_json_string(self):
        """Test conversion of json string to dictionary"""
        json_string = '[{"id": 1, "width": 5, "height": 10, "x": 2, "y": 3}, '
        '{"id": 2, "width": 10, "height": 15, "x": 0, "y": 0}]'
        expected = [{"id": 1, "width": 5, "height": 10, "x": 2, "y": 3},
                    {"id": 2, "width": 10, "height": 15, "x": 0, "y": 0}]
        self.assertEqual(Base.from_json_string(json_string), expected)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_create(self):
        """Test creation of instance from dictionary"""
        r1 = {"id": 1, "width": 5, "height": 10, "x": 2, "y": 3}
        new = Base.create(**

