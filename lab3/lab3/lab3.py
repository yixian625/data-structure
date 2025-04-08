# This module contains the main logic for converting a prefix expression
# to postfix/infix notation. It uses the recursive call build a binary tree from the input,
# then recursively traverse the tree to make the conversion.
# Tracks the performance both for time and peak memory used when processing each line of the file.

from lab3.utils.recursions import *
from lab3.utils.preprocessing import get_stripped_line
import sys
import time
import tracemalloc


def process_file(input_path, output_path, out_format, perf_path=None):
    """
    Function to run the program start to finish. Read from the input file,
    execute the conversion, save results to output path, and optionally save
    the performance metrics if path provided.
    :param input_path: input file path
    :param output_path: output file path
    :param out_format: whether to convert the output to infix or postfix
    :param perf_path: performance file path (optional)
    :return: None
    """
