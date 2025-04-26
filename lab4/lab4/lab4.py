from lab4.QuickSortClass import QuickSort
from lab4.MergeSortClass import MergeSort


def process_file(input_file, return_sorted = False):
    """

    :param input_file:
    :param track_file:
    :param sorted_file:
    :return:
    """

    input_size = 0

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

    with open(input_file, "r") as inputs:

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
        try:
            qs1_instance.quick_sort_basic()
        except RecursionError as e:
            qs1_instance.num_compare = None
            qs1_instance.num_swap = None
            qs1_instance.sorting_method = 'BasicQuickSort'
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
    if return_sorted:
        with open(f"res_{qs1_instance.sorting_method}.txt", 'w') as res:
            if qs1_instance.num_compare is not None:
                for item in qs1_instance.array:
                    res.write(f"{str(item)}\n")
            else:
                res.write("Recursion Error - couldn't complete sorting.")

        with open(f"res_{qs2_instance.sorting_method}.txt", 'w') as res:
            if qs2_instance.num_compare is not None:
                for item in qs2_instance.array:
                    res.write(f"{str(item)}\n")
            else:
                res.write("Recursion Error - couldn't complete sorting.")

        with open(f"res_{qs3_instance.sorting_method}.txt", 'w') as res:
            for item in qs3_instance.array:
                res.write(f"{str(item)}\n")
        with open(f"res_{qs4_instance.sorting_method}.txt", 'w') as res:
            for item in qs4_instance.array:
                res.write(f"{str(item)}\n")
        with open(f"res_{ms_natural.sorting_method}.txt", 'w') as res:
            cur_node = ms_natural.sorted_head
            while cur_node is not None:
                res.write(f"{str(cur_node.data)}\n")
                cur_node = cur_node.next
        with open(f"res_{ms_basic.sorting_method}.txt", 'w') as res:
            cur_node = ms_basic.sorted_head
            while cur_node is not None:
                res.write(f"{str(cur_node.data)}\n")
                cur_node = cur_node.next

    return num_compares, num_swaps


