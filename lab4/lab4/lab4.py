# main function to process the input file, using all the sorting methods available

from lab4.QuickSortClass import QuickSort
from lab4.MergeSortClass import MergeSort
from lab4.utils.input_type_detector import detect_order
import time


def process_file(input_file, return_sorted = False):
    """
    Takes the input file pathname, sort all inputs using each of the sorting methods,
    returns the performance of each sorting methods (i.e, time cost, number of comparisons,
    and number of swaps, and optionally store the sorted result into files.
    :param input_file: file pathname for the input .txt
    :param sorted_file: boolean, whether to save the output files for each sorting method or not. Default to False.
    :return: input specs and performance metrics of all sorting method
    """
    input_name = input_file.stem

    with open(input_file, "r") as inputs:

        input_size = 0
        file_order = detect_order(inputs)

        # initiate class instance for each sort type
        # quick sort: basic
        qs1_instance = QuickSort()
        # quick sort: use median of three as pivot
        qs2_instance = QuickSort()
        # quick sort: insertion sort for size <= 50
        qs3_instance = QuickSort()
        # quick sort: insertion sort for size <= 100
        qs4_instance = QuickSort()
        # natural merge sort
        ms_natural = MergeSort()
        # basic merge sort
        ms_basic = MergeSort()

        for line in inputs:
            input_size += 1
            num = int(line.strip())
            # add input value to the sort instances
            qs1_instance.add_item(num)
            qs2_instance.add_item(num)
            qs3_instance.add_item(num)
            qs4_instance.add_item(num)
            ms_natural.add_node(num)
            ms_basic.add_node(num)

        # apply each sorting method
        time_s1 = time.time()
        try:
            qs1_instance.quick_sort_basic()
        except RecursionError as e:
            qs1_instance.num_compare = None
            qs1_instance.num_swap = None
            qs1_instance.sorting_method = 'BasicQuickSort'
        time1 = time.time() - time_s1

        try:
            qs2_instance.quick_sort_median_of_three()
        except RecursionError as e:
            qs2_instance.num_compare = None
            qs2_instance.num_swap = None
            qs2_instance.sorting_method = 'QuickSortMedianOfThreePivot'

        try:
            qs3_instance.quick_sort_insertion_base50()
        except RecursionError as e:
            qs3_instance.num_compare = None
            qs3_instance.num_swap = None
            qs3_instance.sorting_method = 'QuickSortWithInsertionUnder50'

        try:
            qs4_instance.quick_sort_insertion_base100()
        except RecursionError as e:
            qs4_instance.num_compare = None
            qs4_instance.num_swap = None
            qs4_instance.sorting_method = 'QuickSortWithInsertionUnder100'

        ms_natural.merge_sort_natural()
        ms_basic.merge_sort_basic()

        # get the number of comparisons for each
        num_compares = (qs1_instance.num_compare,
                        qs2_instance.num_compare,
                        qs3_instance.num_compare,
                        qs4_instance.num_compare,
                        ms_natural.num_compare,
                        ms_basic.num_compare)

        # get the number of swaps for each
        num_swaps = (qs1_instance.num_swap,
                     qs2_instance.num_swap,
                     qs3_instance.num_swap,
                     qs4_instance.num_swap,
                     ms_natural.num_swap,
                     ms_basic.num_swap
                     )

        # get time cost for each
        time_cost = (
            qs1_instance.time_cost,
            qs2_instance.time_cost,
            qs3_instance.time_cost,
            qs4_instance.time_cost,
            ms_natural.time_cost,
            ms_basic.time_cost)

        # get the type of method used to sort
        sort_type = (
            qs1_instance.sorting_method,
            qs2_instance.sorting_method,
            qs3_instance.sorting_method,
            qs4_instance.sorting_method,
            ms_natural.sorting_method,
            ms_basic.sorting_method
        )

    if return_sorted:
        with open(f"{input_name}_{qs1_instance.sorting_method}.txt", 'w') as res:
            if qs1_instance.num_compare is not None:
                for item in qs1_instance.array:
                    res.write(f"{str(item)}\n")
            else:
                res.write("Recursion Error - couldn't complete sorting.")

        with open(f"{input_name}_{qs2_instance.sorting_method}.txt", 'w') as res:
            if qs2_instance.num_compare is not None:
                for item in qs2_instance.array:
                    res.write(f"{str(item)}\n")
            else:
                res.write("Recursion Error - couldn't complete sorting.")

        with open(f"{input_name}_{qs3_instance.sorting_method}.txt", 'w') as res:
            if qs3_instance.num_compare is not None:
                for item in qs3_instance.array:
                    res.write(f"{str(item)}\n")
            else:
                res.write("Recursion Error - couldn't complete sorting.")

        with open(f"{input_name}_{qs4_instance.sorting_method}.txt", 'w') as res:
            if qs4_instance.num_compare is not None:
                for item in qs4_instance.array:
                    res.write(f"{str(item)}\n")
            else:
                res.write("Recursion Error - couldn't complete sorting.")

        with open(f"{input_name}_{ms_natural.sorting_method}.txt", 'w') as res:
            cur_node = ms_natural.sorted_head
            while cur_node is not None:
                res.write(f"{str(cur_node.data)}\n")
                cur_node = cur_node.next

        with open(f"{input_name}_{ms_basic.sorting_method}.txt", 'w') as res:
            cur_node = ms_basic.sorted_head
            while cur_node is not None:
                res.write(f"{str(cur_node.data)}\n")
                cur_node = cur_node.next

    return input_size, file_order, sort_type, time_cost, num_compares, num_swaps


