# unittests

import unittest
from lab3.utils.NodeClass import TreeNode
from lab3.utils.PriorityListClass import PriorityArray

class MyTestCase(unittest.TestCase):

    def test_sorting(self):
        node = TreeNode('A', 27)
        node2 = TreeNode('B', 20)
        node3 = TreeNode("C", 21)

        test_array = PriorityArray()
        test_array.insert(node)
        test_array.insert(node2)
        test_array.insert(node3)

        # test insertion and sort
        test_array.sort()

        expected_items = ["B", "C", "A"]
        array_items = [n.item for n in test_array.nodes]

        self.assertEqual(expected_items, array_items)
    #
    def test_pop(self):
        node = TreeNode('A', 27)
        node2 = TreeNode('B', 20)
        node3 = TreeNode("C", 21)

        test_array = PriorityArray()
        test_array.insert(node)
        test_array.insert(node2)
        test_array.insert(node3)

        test_array.sort()

        n = test_array.pop_first()
        self.assertEqual(n.item,'B')

        expected_items = ["C", "A"]
        array_items = [n.item for n in test_array.nodes]
        self.assertEqual(expected_items, array_items)

    def test_ties(self):
        node = TreeNode('AB', 3)
        node2 = TreeNode('CD', 4)
        node3 = TreeNode("E", 4)
        node4 = TreeNode("YZ", 3)

        test_array = PriorityArray()
        test_array.insert(node)
        test_array.insert(node2)
        test_array.insert(node3)
        test_array.insert(node4)

        test_array.sort()

        expected_items = ["AB", "YZ", "E", "CD"]
        array_items = [n.item for n in test_array.nodes]
        self.assertEqual(expected_items, array_items)


if __name__ == '__main__':
    unittest.main()
