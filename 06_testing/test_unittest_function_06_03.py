import unittest
import unittest_function_06_03

class TestUnittestFunction(unittest.TestCase):
    def test_share_result(self):
        self.assertEqual(unittest_function_06_03.share(20, 5), "Each person recieves 4.0.")

    def test_share_string_output(self):
        self.assertIsInstance(unittest_function_06_03.share(20, 5), str)

    def test_share_fail_test(self):
        self.assertNotEqual(unittest_function_06_03.share(20, 5), 4)