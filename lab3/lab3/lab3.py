# This module contains the main logic for generating a Huffman encoding tree from either a frequency table
# or a source text file, then uses this encoding to decode encrypted messages or encode plain text.

import sys
from lab3.DS.HuffmanTreeClass import HuffmanTree


def process_file(source_file, to_encode_file, to_decode_file,
                 tree_map_file, encode_res_file, decode_res_file):

    """
    Takes the source file and generates a Huffman encoding tree. Use the generated
    tree to encode plain text messages and decode binary encryptions encoded using
    the same Huffman encoding tree.
    :param source_file: either a frequency table or a source text to generate frequency table from
    :param to_encode_file: plain text file to encode using the generated Huffman encoding tree
    :param to_decode_file: encrypted messages to decode. Must be encoded using the same Huffman encoding tree
    :param tree_map_file: file name to save the generated Huffman encoding tree to
    :param encode_res_file: file name to save the result for encoding the plain text input
    :param decode_res_file: file name to save the result for decoding the encrypted messages
    :return: None. The function saves the results directly to the corresponding output files
    """

    with source_file.open('r', encoding="utf-8") as source:

        # initiate a tree class
        huffman_tree = HuffmanTree()

        # build the priority array to store the frequencies for all letters
        try:
            huffman_tree.build_priority_array(source)
        except IndexError as e:
            print(f"Error: {e}")
            sys.exit(1)

        # build the huffman encoding tree
        try:
            huffman_tree.build_huffman_encoding_tree()
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)

        # traverse the tree in preorder and save the map
        tree_map = HuffmanTree.preorder_traverse(huffman_tree.tree_root)

        with tree_map_file.open('w') as tree_file:
            tree_file.write("Huffman Encoding Tree in Preorder:\n")
            tree_file.write(tree_map)
            tree_file.write("\n\nEncoding for each character: \n")
            for char in huffman_tree.tree_root.item:
                tree_file.write(f"{char}: {huffman_tree.get_letter_code(char)} \n")

    # encode the input text message
    with to_encode_file.open('r', encoding='utf-8') as encode_input, encode_res_file.open('w', encoding='utf-8') as \
            encode_output:

        for line in encode_input:
            encode_res = ''
            for char in line.strip():
                if char.isalpha():
                    encode_res = encode_res + huffman_tree.get_letter_code(char.upper())
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
                decode_res = huffman_tree.get_decoded_letter(line.strip())
            except IndexError as e:
                print ("The encoded message doesn't match with the frequency table, please table check the source file."
                       "A decoded file cannot be generate.")
                sys.exit(1)
            else:
                decode_output.write(f"Original Encrypted Message: {line.strip()}")
                decode_output.write(f"Decoded Message: \n{decode_res}")
                decode_output.write("\n\n")

