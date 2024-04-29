# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `CustomZeroDivisionError` gets raised correctly.

import unittest
import mymath


class TestMymath(unittest.TestCase):
    def test_subtract_divide_results(self):
        self.assertEqual(mymath.subtract_divide(8, 7, 3), 2)

    def test_custom_zero_division_error(self):
        with self.assertRaises(mymath.CustomZeroDivsionError):
            result = mymath.subtract_divide(8, 7, 7)
        