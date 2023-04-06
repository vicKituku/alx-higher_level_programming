"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_reverse_ordered_list(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_unordered_list(self):
        self.assertEqual(max_integer([3, 5, 1, 4, 2]), 5)

    def test_negative_numbers_list(self):
        self.assertEqual(max_integer([-5, -3, -1, -4, -2]), -1)

    def test_mixed_numbers_list(self):
        self.assertEqual(max_integer([-5, 3, 0, -4, 2]), 3)

    def test_list_with_duplicates(self):
        self.assertEqual(max_integer([1, 2, 3, 3, 2]), 3)


if __name__ == '__main__':
    unittest.main()
