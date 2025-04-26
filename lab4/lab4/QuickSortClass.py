# module containing all the quick sort methods


class QuickSort:

    def __init__(self):
        self.array = []
        self.sorting_method = None
        self.num_compare = 0
        self.num_swap = 0

    def __sizeof__(self):
        return len(self.array)

    def add_item(self, value):
        self.array.append(value)

    def quick_sort_basic(self):
        self._recursive_sort(self.array, 0, len(self.array)-1, pivot_method='first')
        self.sorting_method = 'Basic Quick Sort'

    def quick_sort_median_of_three(self):
        self._recursive_sort(self.array, 0, len(self.array)-1, pivot_method='median_of_three')
        self.sorting_method = 'Quick Sort Median of Three Pivot'

    def quick_sort_insertion_base50(self):
        self._recursive_with_insertion(self.array, 0, len(self.array)-1, 50)
        self.sorting_method = 'Quick Sort with Insertion Under 50'

    def quick_sort_insertion_base100(self):
        self._recursive_with_insertion(self.array, 0, len(self.array)-1, 100)
        self.sorting_method = 'Quick Sort with Insertion Under 100'

    def _recursive_sort(self, array, start, end, pivot_method='first'):
        """
        recursively sort the array
        :param array:
        :param start:
        :param end:
        :param pivot_method
        :return:
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
        :param array:
        :param start:
        :param end:
        :param pivot_method
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
            # copy smaller items to left
            while array[j] >= pivot and i < j:
                self.num_compare += 1
                j -= 1
            if i < j:
                array[i] = array[j]
                self.num_swap += 1

            # copy larger items to right
            while array[i] < pivot and i < j:
                self.num_compare += 1
                i += 1
            if i < j:
                array[j] = array[i]
                self.num_swap += 1

        # when pointers meet, copy pivot to down
        array[i] = pivot

        # return left and right partitions
        return i

    def _insertion_sort(self, array):
        """
        code inspired by: https://www.geeksforgeeks.org/insertion-sort-algorithm/
        :param array:
        :return:
        """

        for i in range(1, len(array)):
            item = array[i]  # item to sort
            j = i - 1  # compare with the item on its left

            while j >= 0 and item < array[j]:
                self.num_compare += 1
                # move the left item to right
                array[j+1] = array[j]
                self.num_swap += 1
                # move the left item pointer to another position to the left
                j -= i

            # place the item when its left is no longer bigger than it
            array[j + 1] = item

    def _recursive_with_insertion(self, array, start, end, min_base_size):
        """

        :param array:
        :param start:
        :param end:
        :param min_base_size:
        :return:
        """

        size = end - start + 1

        if size <= min_base_size:
            self._insertion_sort(array)
            return

        else:
            pivot_index = self._partition(array, start, end)
            # sort left _partition
            self._recursive_sort(array, start, pivot_index - 1)
            # sort right _partition
            self._recursive_sort(array, pivot_index + 1, end)





