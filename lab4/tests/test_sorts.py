import unittest
import random
from lab4.QuickSortClass import QuickSort


class MyTestCase(unittest.TestCase):

    def test_recursive_sort(self):

        array = [2, 4, 1, 7, 9]
        QuickSort.recursive_sort(array, 0, 4)

        self.assertEqual(array, [1, 2, 4, 7, 9])

    def test_sort_with_insertion(self):

        original_array = list(range(1, 201))
        array = original_array.copy()
        random.shuffle(array)

        sort_instance = QuickSort(array)
        sort_instance.quick_sort_insertion_base100()

        sorted_array = sort_instance.array

        self.assertEqual(original_array, sorted_array)
        self.assertEqual('Quick Sort with Insertion Under 100', sort_instance.sorting_method)
    #
    # def test_median_of_three(self):
    #
    #     original_array = list(range(1, 201))
    #     array = original_array.copy()
    #     random.shuffle(array)
    #
    #     sort_instance = QuickSort(array)
    #     sort_instance.quick_sort_median_of_three(array)


if __name__ == '__main__':
    unittest.main()
