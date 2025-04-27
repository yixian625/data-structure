# module containing the natural merge sort class
from lab4.NodeClass import Node
import time


class MergeSort:

    def __init__(self):
        # turn the array containing data to an array of nodes with next pointers (initiated as None)
        self.array = []
        self.sorted_head = None
        self.num_compare = 0
        self.num_swap = 0
        self.sorting_method = None
        self.time_cost = 0

    def __sizeof__(self):
        return len(self.array)

    def add_node(self, item):
        self.array.append(Node(item))

    def merge_sort_basic(self):
        """
        Uses regular merge sort. Implemented as a linked list
        to avoid taking extra space
        :return: the head node of the sorted list
        """
        self.sorting_method = 'BasicMergeSort'
        start_time = time.time()
        head = self._recursive_merge_sort_basic(0, len(self.array)-1)
        self.time_cost = time.time() - start_time
        self.sorted_head = head
        return head

    def merge_sort_natural(self):
        """
        Uses natural merge sort to sort the array.
        :return: the head node of the sorted list.
        """
        self.sorting_method = 'NaturalMergeSort'
        start_time = time.time()
        subfiles_pointers = self._get_natural_subfiles()
        head = self._recursive_natural_merge_sort(subfiles_pointers)
        self.time_cost = time.time() - start_time
        self.sorted_head = head
        return head

    def _recursive_natural_merge_sort(self, start_pointer_list):
        """
        Recursively divides the sub array into two halves and perform merge on the two halves.
        :param start_pointer_list: a list of indices indicating where each subfile starts
        :return: the head node of the sorted list
        """
        # if there's only one subfile, return it directly
        if len(start_pointer_list) == 1:
            return self.array[start_pointer_list[0]]

        # break the subfiles into groups of two recursively
        middle_start_index = len(start_pointer_list)//2
        left_head = self._recursive_natural_merge_sort(start_pointer_list[0:middle_start_index])
        right_head = self._recursive_natural_merge_sort(start_pointer_list[middle_start_index:])

        # return the head of the merged list
        return self._linked_merge(left_head, right_head)

    def _get_natural_subfiles(self):
        """
        :return: a list of indices pointing to the start of each subfile in the array
        """

        start_pointers = [0]

        i = 0
        while i < len(self.array)-1:
            self.num_compare += 1
            # advance the pointer until the item is smaller than the current item
            while i < len(self.array)-1 and self.array[i].data <= self.array[i+1].data:
                self.array[i].next = self.array[i+1] # set up the next pointers for nodes within each subfile
                self.num_swap += 1
                i += 1
            # move pointer one move place to the right to start the new subfile
            if i != len(self.array)-1:
                i += 1
                start_pointers.append(i)

        return start_pointers

    def _recursive_merge_sort_basic(self, array_start, array_end):
        """
        Recursively divides the array by halves and merges the two halves in a sorted way
        :param array_start: the index for the start item of the array to be sorted
        :param array_end: the index for the end item of the array to be sorted
        :return: the head node of the sorted list
        """
        if array_start == array_end:
            return self.array[array_start]  # only one element

        middle = array_start + (array_end - array_start) // 2

        left_head = self._recursive_merge_sort_basic(array_start, middle)
        right_head = self._recursive_merge_sort_basic(middle + 1, array_end)

        # return the head of the merged list
        return self._linked_merge(left_head, right_head)

    def _linked_merge(self, head1, head2):
        """
        Merges two linked lists in a sorted manner given the head nodes.
        code inspired by: https://stackoverflow.com/questions/7685/merge-sort-a-linked-list
        :param head1: the head node of the first linked list
        :param head2: the head node of the second linked list
        :return:
        """
        dummy = Node(0)  # dummy head; keep track of array head
        tail = dummy     # pointer to the last element of the linked list

        while head1 and head2:
            self.num_compare += 1
            if head1.data < head2.data:
                tail.next = head1
                head1 = head1.next
                self.num_swap += 1
            else:
                tail.next = head2
                head2 = head2.next
                self.num_swap += 1

            tail = tail.next

        # Attach the remainder
        tail.next = head1 if head1 else head2

        return dummy.next  # return actual head of merged list

