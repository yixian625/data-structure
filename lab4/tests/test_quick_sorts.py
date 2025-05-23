import unittest
import random
from lab4.QuickSortClass import QuickSort


class MyTestCase(unittest.TestCase):

    def test_recursive_sort(self):

        array = [2, 4, 1, 7, 9]
        sort_instance = QuickSort()
        for i in array:
            sort_instance.add_item(i)
        sort_instance._recursive_sort(sort_instance.array, 0, 4)

        self.assertEqual(sort_instance.array, [1, 2, 4, 7, 9])

    def test_sort_with_insertion(self):

        original_array = list(range(1, 201))
        array = original_array.copy()
        random.shuffle(array)

        sort_instance = QuickSort()
        for i in array:
            sort_instance.add_item(i)

        sort_instance.quick_sort_insertion_base100()

        sorted_array = sort_instance.array

        self.assertEqual(original_array, sorted_array)
        self.assertEqual('QuickSortWithInsertionUnder100', sort_instance.sorting_method)

    def test_median_of_three(self):

        original_array = list(range(1, 201))
        array = original_array.copy()
        random.shuffle(array)

        sort_instance = QuickSort()
        for i in array:
            sort_instance.add_item(i)
        sort_instance.quick_sort_median_of_three()
        sorted_array = sort_instance.array

        self.assertEqual(original_array, sorted_array)
        self.assertEqual('QuickSortMedianOfThreePivot', sort_instance.sorting_method)


if __name__ == '__main__':
    unittest.main()
