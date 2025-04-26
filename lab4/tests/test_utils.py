import unittest
from lab4.utils.input_type_detector import detect_order

class MyTestCase(unittest.TestCase):
    def test_detect_order(self):
        with open('resources/inputs/asc_50.txt', 'r') as file:
            self.assertEqual(detect_order(file), 'Ascending')  # add assertion here

        with open('resources/inputs/desc_50.txt', 'r') as file:
            self.assertEqual(detect_order(file), 'Descending')  # add assertion here

        with open('resources/inputs/rand_50.txt', 'r') as file:
            self.assertEqual(detect_order(file), 'Random')  # add assertion here


if __name__ == '__main__':
    unittest.main()
