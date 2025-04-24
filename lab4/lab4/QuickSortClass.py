# module containing all the quick sort methods


class QuickSort:

    def __init__(self, array):
        self.array = array
        self.sorting_method = None

    def basic_quick_sort(self):
        QuickSort.recursive_sort(self.array, 0, len(self.array)-1)
        self.sorting_method = 'Basic Quick Sort'

    def quick_sort_insertion_base50(self):
        QuickSort.recursive_with_insertion(self.array, 0, len(self.array)-1, 50)
        self.sorting_method = 'Quick Sort with Insertion Under 50'

    def quick_sort_insertion_base100(self):
        QuickSort.recursive_with_insertion(self.array, 0, len(self.array)-1, 100)
        self.sorting_method = 'Quick Sort with Insertion Under 100'



    @staticmethod
    def recursive_sort(array, start, end):
        """
        recursively sort the array
        :param array:
        :param start:
        :param end:
        :return:
        """
        size = end - start + 1

        # base cases
        if size <= 1:
            return
        elif size == 2:
            # swap if needed for array size of 2
            if array[start] > array[end]:
                array[start], array[end] = array[end], array[start]
                return
        else:
            pivot_index = QuickSort.partition(array, start, end)
            # sort left partition
            QuickSort.recursive_sort(array, start, pivot_index - 1)
            # sort right partition
            QuickSort.recursive_sort(array, pivot_index + 1, end)

    @staticmethod
    def partition(array, start, end):
        """
        :param array:
        :param start:
        :param end:
        :return: return the pivot index. Make in-place changes to array.
        """
        # choose the pivot accordingly
        # use the first item
        pivot = array[start]
        i = start   # down pointer
        j = end  # up pointer

        while i < j:
            # copy smaller items to left
            while array[j] >= pivot and i < j:
                j -= 1
            if i < j:
                array[i] = array[j]

            # copy larger items to right
            while array[i] < pivot and i < j:
                i += 1
            if i < j:
                array[j] = array[i]

        # when pointers meet, copy pivot to down
        array[i] = pivot

        # return left and right partitions
        return i

    @staticmethod
    def insertion_sort(array):

        for i in range(1, len(array)):
            item = array[i]  # item to sort
            j = i - 1  # compare with the item on its left

            while j >= 0 and item < array[j]:
                # move the left item to right
                array[j+1] = array[j]
                # move the left item pointer to another position to the left
                j -= i

            # place the item when its left is no longer bigger than it
            array[j + 1] = item

    @staticmethod
    def recursive_with_insertion(array, start, end, min_base_size):
        """

        :param array:
        :param start:
        :param end:
        :param min_base_size:
        :return:
        """

        size = end - start + 1

        if size <= min_base_size:
            QuickSort.insertion_sort(array)
            return

        else:
            pivot_index = QuickSort.partition(array, start, end)
            # sort left partition
            QuickSort.recursive_sort(array, start, pivot_index - 1)
            # sort right partition
            QuickSort.recursive_sort(array, pivot_index + 1, end)





