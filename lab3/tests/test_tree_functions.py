import unittest
from lab3.utils.NodeClass import TreeNode
from lab3.utils.PriorityListClass import PriorityArray
from lab3.utils.TreeFunctions import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        node = TreeNode('A', 27)
        node2 = TreeNode('B', 20)
        node3 = TreeNode("C", 21)

        self.test_array = PriorityArray()
        self.test_array.insert(node)
        self.test_array.insert(node2)
        self.test_array.insert(node3)

        # test insertion and sort
        self.test_array.sort()

        # build the Huffman encoding tree by merging different nodes
        while len(self.test_array) > 1:
            left_node = self.test_array.pop_first()
            right_node = self.test_array.pop_first()
            merged_node = left_node + right_node

            # put the new merged node back to the priority array to
            # keep track of its new priority
            self.test_array.insert(merged_node)
            self.test_array.sort()

    def test_preorder_traverse(self):
        root = self.test_array.nodes[0]
        tree_map = preorder_traverse(root)
        expected_map = f"ABC:68 A:27 BC:41 B:20 C:21 "
        self.assertEqual(tree_map, expected_map)


if __name__ == '__main__':
    unittest.main()
