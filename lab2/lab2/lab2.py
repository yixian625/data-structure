# This module contains the main logic for converting a prefix expression
# to postfix notation. It relies on stack-based processing and calls
# various utility functions for text processing, validation, and performance tracking.

from lab2.utils.measures import get_performance
from lab2.utils.recursions import recur_tree
import sys


@get_performance
def recur_pre_to_post(node):

    """
    Given the binary tree for the input prefix, traverse the tree
    and return the postfix expression of the input
    :param node: the root node of the binary tree
    :return: postfix expression
    """

    if node.type == 'opd':
        return node.item
    else:
        left_opd = recur_pre_to_post(node.left_child)
        right_opd = recur_pre_to_post(node.right_child)

        # when @get_performance is applied, function returns a tuple
        # extract the postfix (first item in tuple)
        if isinstance(left_opd, tuple):
            left_opd = left_opd[0]
        if isinstance(right_opd, tuple):
            right_opd = right_opd[0]

        return left_opd + right_opd + node.item


def process_file(input_path, output_path, perf_path=None):
    """
    Function to run the program start to finish. Read from the input file,
    execute the conversion, save results to output path, and optionally save
    the performance metrics if path provided.
    :param input_path: input file path
    :param output_path: output file path
    :param perf_path: performance file path (optional)
    :return: None
    """

    performance_tracking = []

    with input_path.open('r') as input_file, output_path.open('w') as output_file:

        output_file.write("Input | Output \n")
        output_file.write("-" * 30 + "\n")

        for line in input_file:

            # create binary tree for the input
            tree_root_node, char_count = recur_tree(iter(line))

            # convert to prefix & get performance
            postfix, status, time_used, memory_used = recur_pre_to_post(tree_root_node)
            output_file.write(f"{line} | {postfix} \n")
            performance_tracking.append((char_count, time_used, memory_used, status, line))

        # if all lines have been skipped for being empty, raise error
        if len(performance_tracking) == 0:
            print("You have passes an empty file. Nothing will be returned in the output file.")
            sys.exit(1)

        # get summary stats for entire input file
        total_size = sum(s for s, _, _, _, _ in performance_tracking)
        total_time = sum(t for _, t, _, _, _ in performance_tracking)
        total_memory = sum(m for _, _, m, _, _ in performance_tracking)

        output_file.write(f"\nTotal {total_time: .3f} ms and {total_memory: .3f} KB of memory used to process the"
                          f" input the size of {total_size} characters.\n")
        if total_size != 0:
            output_file.write(f"averaging {total_time / total_size: .3f} ms and "
                              f"{total_memory / total_size: .3f} KB of memory used per character of input.")

    if perf_path:
        with perf_path.open('w') as perf_file:
            perf_file.write("Line | Input Size (# chars) | Time (ms) | Memory (KB) | Completion Status\n")
            for input_size, time_used, memory_used, status, input_string in performance_tracking:
                perf_file.write(f"{input_string} | {input_size} | {time_used:.3f} | {memory_used:.3f} | {status}\n")
