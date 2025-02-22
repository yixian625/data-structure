import unittest
from lab1.lab1 import prefix_to_postfix


class MyTestCase(unittest.TestCase):

    def test_pre_to_post_valid(self):
        prefix = '$+-ABC+D-EF'
        # the prefix_to_postfix is wrapped by a decorator function
        # the first item returned is the postfix
        postfix = prefix_to_postfix(prefix)[0]
        self.assertEqual(postfix, "AB-C+DEF-+$")

    def test_pre_to_post_valid_with_digits(self):
        prefix = '//20 100$+-ABC+D-EF'
        postfix = prefix_to_postfix(prefix)[0]
        self.assertEqual(postfix, "20 100 /AB-C+DEF-+$/")

    def test_pre_to_post_invalid_prefix(self):
        prefix = '/A+BC +C*BA'
        error_msg = "Error: Input prefix is invalid. Not enough operators."
        # too few operators, should raise error
        self.assertEqual(prefix_to_postfix(prefix)[0], error_msg)

    def test_pre_to_post_illegal_char(self):
        prefix = '$%-ABC+D-EF'
        error_msg = f"Error: One or more illegal characters in the input string. " \
                    f"Only letters and +,-,*,/,$,^ are allowed."
        # illegal symbol %, should rais error
        self.assertEqual(prefix_to_postfix(prefix)[0], error_msg)


if __name__ == '__main__':
    unittest.main()
