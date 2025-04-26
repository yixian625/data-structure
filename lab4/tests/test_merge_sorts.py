import unittest
import random
from lab4.NodeClass import Node
from lab4.MergeSortClass import MergeSort


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.items = list(range(100))
        random.shuffle(self.items)

    def test_recur_merge_basic(self):

        merge_instance = MergeSort()
        for i in self.items:
            merge_instance.add_node(i)

        merge_instance.merge_sort_basic()

        sorted_list = []
        cur_node = merge_instance.sorted_head
        while cur_node is not None:
            sorted_list.append(cur_node.data)
            cur_node = cur_node.next

        self.assertEqual(sorted_list, list(range(100)))  # add assertion here

    def test_natural_merge_subfile_creation(self):
        items = [0, 1, 5, 2, 10, 9, 11, 7, 99, 20]
        expected_pointers = [0, 3, 5, 7, 9]

        merge_instance = MergeSort()
        for i in items:
            merge_instance.add_node(i)

        returned_pointers = merge_instance._get_natural_subfiles()

        self.assertEqual(expected_pointers, returned_pointers)

    def test_natural_merge(self):

        merge_array_instance = MergeSort()
        for i in self.items:
            merge_array_instance.add_node(i)

        merge_array_instance.merge_sort_natural()

        sorted_list = []
        cur_node = merge_array_instance.sorted_head
        while cur_node is not None:
            sorted_list.append(cur_node.data)
            cur_node = cur_node.next

        self.assertEqual(sorted_list, list(range(100)))  # add assertion here


if __name__ == '__main__':
    unittest.main()
