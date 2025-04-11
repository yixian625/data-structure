# This module contains the main logic for converting a prefix expression
# to postfix/infix notation. It uses the recursive call build a binary tree from the input,
# then recursively traverse the tree to make the conversion.
# Tracks the performance both for time and peak memory used when processing each line of the file.


import sys
import time
import tracemalloc

from lab3.utils.NodeClass import TreeNode
from lab3.utils.PriorityListClass import PriorityArray
from lab3.utils.TreeFunctions import preorder_traverse, get_letter_code, get_decoded_letter
from lab3.utils.TableCreater import detect_table, create_freq_table


def process_file(source_file, to_encode_file, to_decode_file,
                 tree_map_file, encode_res_file, decode_res_file):

    """

    :param source_file:
    :param to_encode_file:
    :param to_decode_file:
    :param tree_map_file:
    :param encode_res_file:
    :param decode_res_file:
    :return:
    """

    with source_file.open('r', encoding="utf-8") as source:

        # initialize an array to store nodes based on priority
        priority_array = PriorityArray()

        # determine whether a freq table or source text has been passed as input
        source_file_type = detect_table(source)

        # process the frequencies if it's a table
        if source_file_type == "Table":
            for line in source:
                content = line.strip().split(" - ")
                if content[0].isalpha() and content[1].isdigit():
                    node = TreeNode(char=content[0], freq=int(content[1]))
                    priority_array.insert(node)
                else:
                    print("Your frequency table is not in the right format. Please follow the following \
                           example: \"A - 10\"")
                    sys.exit(1)

        # build the freq table if the input is a source text
        elif source_file_type == "Text":
            freq_array = create_freq_table(source)
            # because the frequencies are saved in the same order as alphabets
            # and the upper-case letters starts from ascii 65, the actual letter is i+65 in ascii
            for i in range(len(freq_array)):
                # check if there are letters not represented in the source text
                if freq_array[i] == 0:
                    print(f"Your source text doesn't contain all letters. "
                          f"There is no {chr(i+65)} in the file. Please change a source.")
                    sys.exit(1)
                else:
                    node = TreeNode(char=chr(i+65), freq=freq_array[i])
                    priority_array.insert(node)

        # sort all nodes based on priority
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
            encode_res = ''
            for char in line.strip():
                if char.isalpha():
                    encode_res = encode_res + get_letter_code(final_root, char.upper())
            encode_output.write(f"Original Message: {line.strip()}\n")
            encode_output.write(f"Encrypted Message: {encode_res}\n")
            original_size = len(line.strip().encode("utf-8"))
            compressed_size = len(encode_res)//8  # packed into bytes
            encode_output.write(f'Original size: {original_size} bytes. '
                                f'Encrypted size (packed in bytes): {compressed_size} bytes. '
                                f'Compressed to {compressed_size/original_size: .0%} of original size.')
            encode_output.write("\n\n")

    # decode the encrypted message
    with to_decode_file.open('r') as decode_input, decode_res_file.open('w') as decode_output:

        for line in decode_input:
            try:
                decode_res = get_decoded_letter(final_root, line.strip())
            except IndexError as e:
                print ("The encoded message doesn't match with the frequency table, please table check the source file."
                       "A decoded file cannot be generate.")
                sys.exit(1)
            else:
                decode_output.write(f"Original Encrypted Message: {line.strip()}")
                decode_output.write(f"Decoded Message: \n{decode_res}")
                decode_output.write("\n\n")

