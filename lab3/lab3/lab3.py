# This module contains the main logic for converting a prefix expression
# to postfix/infix notation. It uses the recursive call build a binary tree from the input,
# then recursively traverse the tree to make the conversion.
# Tracks the performance both for time and peak memory used when processing each line of the file.

#from lab3.utils.recursions import *
#from lab3.utils.preprocessing import get_stripped_line
import sys
import time
import tracemalloc

from lab3.utils.NodeClass import TreeNode
from lab3.utils.PriorityListClass import PriorityArray
from lab3.utils.TreeFunctions import preorder_traverse, get_letter_code


def process_file(freq_table_file, tree_map_file, to_encode_file,
                 encode_res_file):

    """

    :param freq_table_file:
    :return:
    """

    with freq_table_file.open('r') as freq_table:

        # initialize an array to store nodes based on priority
        priority_array = PriorityArray()

        # use the priority array to store and sort the nodes
        for line in freq_table:
            content = line.split(" - ")
            node = TreeNode(char = content[0], freq=int(content[1].strip()))
            priority_array.insert(node)

        priority_array.sort()

        # build the Huffman encoding tree by merging different nodes
        while len(priority_array) > 1:

            left_node = priority_array.pop_first()
            right_node = priority_array.pop_first()
            merged_node = left_node + right_node

            # put the new merged node back to the priority array to
            # keep track of its new priority
            priority_array.insert(merged_node)
            priority_array.sort()

        final_root = priority_array.nodes[0]

        # get the traverse the tree in preorder and save the map
        tree_map = preorder_traverse(final_root)

        with tree_map_file.open('w') as tree_file:
            tree_file.write("Huffman Encoding Tree in Preorder:\n")
            tree_file.write(tree_map)
            tree_file.write("\n\nEncoding for each character: \n")
            for char in final_root.item:
                tree_file.write(f"{char}: {get_letter_code(final_root, char)} \n")

    # encode the input text message
    with to_encode_file.open('r') as encode_input, encode_res_file.open('w') as encode_output:

        for line in encode_input:
            print(line)
            encode_res = ''
            for char in line:
                if char.isalpha():
                    encode_res = encode_res + get_letter_code(final_root, char.upper())
            encode_output.write(f"Original Message: {line.strip()}\n")
            encode_output.write(encode_res)
            encode_output.write("\n\n")












# def process_file(input_path, output_path, out_format, perf_path=None):
#     """
#     Function to run the program start to finish. Read from the input file,
#     execute the conversion, save results to output path, and optionally save
#     the performance metrics if path provided.
#     :param input_path: input file path
#     :param output_path: output file path
#     :param out_format: whether to convert the output to infix or postfix
#     :param perf_path: performance file path (optional)
#     :return: None
#     """
#
