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


##create test class for the file being imported
class TestExample(unittest.TestCase):
    ## add test for a division function
    def test_divide(self):
        self.assertEqual(example.divide(10, 5), 2)
    
    ## add test for a multiplication function
    def test_multiply(self):
        self.assertEqual(example.multiply(5, 4), 20)
