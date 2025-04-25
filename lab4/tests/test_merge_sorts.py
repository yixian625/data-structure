import unittest
import random
from lab4.NodeClass import Node
from lab4.MergeSortClass import MergeSort


class MyTestCase(unittest.TestCase):

    def setUp(self):
        items = list(range(100))
        random.shuffle(items)
        self.node_array = [Node(i) for i in items]

    def test_recur_merge_basic(self):

        array = self.node_array.copy()

        sorted_head = MergeSort._recursive_merge_sort_basic(array, 0, len(array)-1)

        sorted_list = []
        cur_node = sorted_head
        while cur_node is not None:
            sorted_list.append(cur_node.data)
            cur_node = cur_node.next

        self.assertEqual(sorted_list, list(range(100)))  # add assertion here


if __name__ == '__main__':
    unittest.main()
