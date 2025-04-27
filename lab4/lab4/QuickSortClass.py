# module containing all the quick sort methods
import time


class QuickSort:

    def __init__(self):
        self.array = []
        self.time_cost = 0
        self.sorting_method = None
        self.num_compare = 0
        self.num_swap = 0

    def __sizeof__(self):
        return len(self.array)

    def add_item(self, value):
        """
        Adds a new value to the array.
        :param value: the new value to be added
        :return: None. Self.array is updated with the new value added.
        """
        self.array.append(value)

    def quick_sort_basic(self):
        """
        Uses basic quick sort to sort the array.
        :return: None. Self.array is updated with the new value added.
        """
        start = time.time()
        self._recursive_sort(self.array, 0, len(self.array)-1, pivot_method='first')
        self.sorting_method = 'BasicQuickSort'
        self.time_cost = time.time() - start

    def quick_sort_median_of_three(self):
        """
        Uses the median-of-three as the pivot in quick sort to sort the array.
        :return: None. Self.array is updated with the new value added.
        """
        start = time.time()
        self._recursive_sort(self.array, 0, len(self.array)-1, pivot_method='median_of_three')
        self.sorting_method = 'QuickSortMedianOfThreePivot'
        self.time_cost = time.time() - start

    def quick_sort_insertion_base50(self):
        """
        Uses quick sort until the subarray has 50 or fewer items, then uses insertion sort to sort it.
        :return: None. Self.array is updated with the new value added.
        """
        start = time.time()
        self._recursive_with_insertion(self.array, 0, len(self.array)-1, 50)
        self.sorting_method = 'QuickSortWithInsertionUnder50'
        self.time_cost = time.time() - start

    def quick_sort_insertion_base100(self):
        """
        Uses quick sort until the subarray has 100 or fewer items, then uses insertion sort to sort it.
        :return: None. Self.array is updated with the new value added.
        """
        start = time.time()
        self._recursive_with_insertion(self.array, 0, len(self.array)-1, 100)
        self.sorting_method = 'QuickSortWithInsertionUnder100'
        self.time_cost = time.time() - start

    def _recursive_sort(self, array, start, end, pivot_method='first'):
        """
        Recursively sort the array using quick sort until the base cases where the sub-array contains 1 or 2 items.
        :param array: the array to be sorted
        :param start: the start index for items to be sorted in the array
        :param end: the end index for items to be sorted in the array
        :param pivot_method: whether to use the 1st item as pivot (default) or the median-of-three.
        :return: None. The array is updated with the items sorted.
        """
        size = end - start + 1

        # base cases
        if size <= 1:
            return
        elif size == 2:
            # swap if needed for array size of 2
            self.num_compare += 1
            if array[start] > array[end]:
                array[start], array[end] = array[end], array[start]
                self.num_swap += 1
                return
        else:
            pivot_index = self._partition(array, start, end, pivot_method=pivot_method)
            # sort left _partition
            self._recursive_sort(array, start, pivot_index - 1, pivot_method=pivot_method)
            # sort right _partition
            self._recursive_sort(array, pivot_index + 1, end, pivot_method=pivot_method)

    def _partition(self, array, start, end, pivot_method='first'):
        """
        Recursively partition the part of the array from the "star" index to the "end" index.
        :param array: the array to be sorted
        :param start: the start index for items to be sorted in the array
        :param end: the end index for items to be sorted in the array
        :param pivot_method: whether to use the 1st item as pivot (default) or the median-of-three.
        :return: return the pivot index. Make in-place changes to array.
        """
        i = start   # down pointer
        j = end  # up pointer

        # choose the pivot accordingly
        # use the first item
        if pivot_method == 'first':
            pivot = array[start]
        else:
            # use median of three
            mid = i + (j - i) // 2
            candidates = [array[i], array[j], array[mid]]
            self._insertion_sort(candidates)
            pivot = candidates[1]
            # swap the pivot to the beginning of the array for
            # the partition logic to work
            pivot_index = array.index(pivot)
            array[start], array[pivot_index] = array[pivot_index], array[start]
            self.num_swap += 1

        while i < j:
            self.num_compare += 1
            # copy smaller items to left
            while array[j] >= pivot and i < j:
                j -= 1
            if i < j:
                array[i] = array[j]
                self.num_swap += 1

            # copy larger items to right
            while array[i] < pivot and i < j:
                i += 1
            if i < j:
                array[j] = array[i]
                self.num_swap += 1

        # when pointers meet, copy pivot to down
        array[i] = pivot

        # return left and right partitions
        return i

    def _insertion_sort(self, array, start=0, end=None):
        """
        Performs insertion sort on an array.
        code inspired by: https://www.geeksforgeeks.org/insertion-sort-algorithm/
        :param array: the array to be sorted.
        :return: None. The array is updated to the sorted order.
        """
        if end is None:
            end = len(array) - 1

        for i in range(start+1, end+1):
            item = array[i]  # item to sort
            j = i - 1  # compare with the item on its left
            self.num_compare += 1

            while j >= 0 and item < array[j]:
                # move the left item to right
                array[j+1] = array[j]
                self.num_swap += 1
                # move the left item pointer to another position to the left
                j -= 1

            # place the item when its left is no longer bigger than it
            array[j + 1] = item

    def _recursive_with_insertion(self, array, start, end, min_base_size):
        """
        Recursively uses quick sort to sort part of an array given the start and end index of the items to be sorted.
        Once the sub-array gets under the minimum base size, switches over to use insertion sort to finish the sorting.
        :param array: the array to be sorted
        :param start: the start index for items to be sorted in the array
        :param end: the end index for items to be sorted in the array
        :param min_base_size: the size threshold for the sub-array to be sorted by insertion sort.
        :return:  None. The array is updated to the sorted items.
        """

        size = end - start + 1

        if size <= min_base_size:
            self._insertion_sort(array)
            return

        else:
            pivot_index = self._partition(array, start, end)
            # sort left _partition
            self._recursive_with_insertion(array, start, pivot_index - 1, min_base_size)
            # sort right _partition
            self._recursive_with_insertion(array, pivot_index + 1, end, min_base_size)





