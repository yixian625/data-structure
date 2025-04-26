import unittest
import random
from lab4.NodeClass import Node
from lab4.MergeSortClass import MergeSort


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.items = list(range(100))
        random.shuffle(self.items)

    def test_recur_merge_basic(self):

        array = [Node(i) for i in self.items]

        sorted_head = MergeSort._recursive_merge_sort_basic(array, 0, len(array)-1)

        sorted_list = []
        cur_node = sorted_head
        while cur_node is not None:
            sorted_list.append(cur_node.data)
            cur_node = cur_node.next

        self.assertEqual(sorted_list, list(range(100)))  # add assertion here

    def test_natural_merge_subfile_creation(self):
        items = [0, 1, 5, 2, 10, 9, 11, 7, 99, 20]
        expected_pointers = [0, 3, 5, 7, 9]
        node_array = [Node(i) for i in items]
        returned_pointers = MergeSort._get_natural_subfiles(node_array)

        self.assertEqual(expected_pointers, returned_pointers)

    def test_natural_merge(self):

        merge_array_instance = MergeSort()
        for i in self.items:
            merge_array_instance.add_node(i)

        sorted_head = merge_array_instance.merge_sort_natural()

        sorted_list = []
        cur_node = sorted_head
        while cur_node is not None:
            sorted_list.append(cur_node.data)
            cur_node = cur_node.next

        self.assertEqual(sorted_list, list(range(100)))  # add assertion here


if __name__ == '__main__':
    unittest.main()
