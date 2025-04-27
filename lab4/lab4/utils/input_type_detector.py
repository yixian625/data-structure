from lab4.MergeSortClass import MergeSort


def detect_order(input_file):
    """
    Detectors whether the inputs are in ascending, descending, or random orders
    :param input_file: the input .txt file
    :return: whether the file contains inputs in ascending, descending, or random order.
    """

    num_list = []
    try:
        for i in range(0, 5):
            line = input_file.readline()
            num_list.append(int(line.strip()))
        input_file.seek(0) # return to the beginning of the file

    except ValueError as e:
        raise ValueError("Please make sure your inputs are integers")

    except IndexError as e:
        raise IndexError("Please make sure your input file contains more than 5 numbers")

    else:
        asc_list = []
        desc_list = []

        # get the expected ascending order given the input items
        temp_array = MergeSort()
        for i in num_list:
            temp_array.add_node(i)
        temp_array.merge_sort_natural()
        cur_node = temp_array.sorted_head
        while cur_node is not None:
            asc_list.append(cur_node.data)
            cur_node = cur_node.next

        # get the expected descending order
        for i in range(len(asc_list)-1, -1, -1):
            desc_list.append(asc_list[i])

        # check to see whether the orginal list was sorted or not
        if num_list == asc_list:
            return 'Ascending'

        elif num_list == desc_list:
            return 'Descending'

        else:
            return 'Random'

