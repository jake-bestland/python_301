# Write a script that demonstrates TDD. Using pseudocode, plan out
# a couple of small functions. They could be as fundamental as adding
# and subtracting numbers with each other,
# or more complex such as functions that read and write to files.
#
# Instead of writing the functions, however, only write the tests for them.
# Think about how your functions might fail and write tests that will check 
# for that and identify these failures.
#
# You do not need to implement the actual functions after writing the tests 
# but of course you can do that, too.

import unittest
import example  ## file doesn't exist, just for demonstration


class TestExample(unittest.TestCase):
    ## add test for an addition function
    def test_addition(self):
        self.assertEqual(example.addition(5, 4), 9)
    
    ## add test for a multiplication function
    def test_multiply(self):
        self.assertEqual(example.multiply(5, 4), 20)
