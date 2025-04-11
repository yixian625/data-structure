import unittest
from lab3.utils.TableCreater import *


class MyTestCase(unittest.TestCase):

    def test_tree_creator(self):

        text = "It is getting late"
        freq_list = create_freq_table(text)
        self.assertTrue(sum(freq_list) == 15)

        # there are two Es (index =4)
        # and four Ts
        self.assertTrue(freq_list[4] == 2)
        self.assertTrue(freq_list[19] == 4)

if __name__ == '__main__':
    unittest.main()
