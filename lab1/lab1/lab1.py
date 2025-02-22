# This module contains the main logic for converting a prefix expression
# to postfix notation. It relies on stack-based processing and calls
# various utility functions for text processing, validation, and performance tracking.

from lab1.utils.input_processing import get_stripped_line, gather_digits, get_char_type
from lab1.utils.stack_operation import process_char_with_stack
from lab1.utils.measures import get_performance
from lab1.stack import Stack
import sys


@get_performance  # track the performance for each call on the function
def prefix_to_postfix(input_string) -> str:
    """
    Convert the given input prefix string to postfix string.
    :param input_string: the input prefix string
    :return: the postfix string
    """
    # stack for conversion
    cur_stack = Stack()

    # stack for processing the characters from right to left
    line_stack = Stack()

    for char in input_string:
        line_stack.push(char)

    # if there's an empty line, return an empty line
    if line_stack.is_empty():
        return ""

    while not line_stack.is_empty():
        char = line_stack.pop()  # read the line from right to left
        if char == " ":  # skip if it's an empty space
            continue
        if char == '^':  # convert to the exponential mark recognized by the algorithm
            char = '$'
        # all digits next to each other are considered to be
        # a single number. Gather them together as one before moving on
        if char.isdigit():
            char, line_stack = gather_digits(char, line_stack)
            char_type = 'opd'
        else:
            char_type = get_char_type(char)
        cur_stack = process_char_with_stack(char, char_type, cur_stack)

    postfix = cur_stack.pop()

    if not cur_stack.is_empty():
        raise ValueError("Input prefix is invalid. Not enough operators.")

    return postfix


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
            # get the trimmed line; returns None if all empty in a line
            input_string, char_count = get_stripped_line(line)
            # skip a line if there is nothing but empty spaces
            if input_string is None:
                continue
            postfix, status, time_used, memory_used = prefix_to_postfix(input_string)
            output_file.write(f"{input_string} | {postfix} \n")
            performance_tracking.append((char_count, time_used, memory_used, status, input_string))

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
