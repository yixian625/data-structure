# This module the class definition for the Huffman encoding tree and its associated methods,
# including building the priority array for the letters, building the tree, and traversing the tree

from lab3.DS.PriorityListClass import PriorityArray
from lab3.DS.NodeClass import TreeNode
from lab3.utils.TableCreater import *


class HuffmanTree:

    def __init__(self):
        self.tree_root = None
        self.priority_array = None

    def build_priority_array(self, source):
        """
        Store all letters and their frequencies in an array as tree nodes and sort it
        :param source: source file - a frequency table or a source text file to build the frequency table from
        :return: update self.priority_array with all the nodes inserted and sorted
        """
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
                    raise ValueError("Your frequency table is not in the right format. Please follow the following \
                           example: \"A - 10\"")
                    # sys.exit(1)

        # build the freq table if the input is a source text
        elif source_file_type == "Text":
            freq_array = create_freq_table(source)
            # because the frequencies are saved in the same order as alphabets
            # and the upper-case letters starts from ascii 65, the actual letter is i+65 in ascii
            for i in range(len(freq_array)):
                # check if there are letters not represented in the source text
                if freq_array[i] == 0:
                    raise ValueError(f"Your source text doesn't contain all letters. "
                          f"There is no {chr(i+65)} in the file. Please change a source.")
                    # sys.exit(1)
                else:
                    node = TreeNode(char=chr(i+65), freq=freq_array[i])
                    priority_array.insert(node)

        # sort all nodes based on priority
        priority_array.sort()

        # update the priority array attribute of the class
        self.priority_array = priority_array

    def build_huffman_encoding_tree(self):
        """
        Builds the huffman encoding tree from the priority array list
        :return: updates the root_node parameter to the root node of the final tree
        """
        # build the Huffman encoding tree by merging different nodes
        while len(self.priority_array) > 1:

            left_node = self.priority_array.pop_first()
            right_node = self.priority_array.pop_first()
            merged_node = left_node + right_node

            # put the new merged node back to the priority array to
            # keep track of its new priority
            self.priority_array.insert(merged_node)
            self.priority_array.sort()

        self.tree_root = self.priority_array.nodes[0]

    @staticmethod
    def preorder_traverse(node: TreeNode) -> str:
        """
        Takes the root node of the Huffman encoding tree and print
        out the encoding with recursive calls.
        :param node: the root node of a tree/subtree
        :return: a string describing the tree structure (node item:item frequency) in preorder
        """
        # base case -
        # strict binary tree, if no left_child, there's no right child either
        if node.left_child is None:
            return f"{node.item}:{node.freq} "
        else:
            left_tree = HuffmanTree.preorder_traverse(node.left_child)
            right_tree = HuffmanTree.preorder_traverse(node.right_child)
            sub_tree = f"{node.item}:{node.freq} " + left_tree + right_tree

            return sub_tree

    def get_letter_code(self, char) -> str:
        """
        Traverse the tree to find the input character, return the Huffman code for that
        character.
        :param char: character to get the code for
        :return: the Huffman code for that character
        """

        cur_node = self.tree_root
        char_code = ''
        while cur_node.left_child is not None:
            if char in cur_node.left_child.item:
                char_code = char_code + '0'
                cur_node = cur_node.left_child
            else:
                char_code = char_code + '1'
                cur_node = cur_node.right_child

        return char_code

    def get_decoded_letter(self, input_digits) -> str:
        """
        Takes a string of digits. Traverse the tree based on the digits and return
        the decoded message
        :param input_digits: encrypted message in the form of a string of digits
        :return: the decoded message in alphabets
        """
        cur_node = self.tree_root
        decode_res = ''
        index = 0

        while index < len(input_digits):
            # Traverse down the tree until a leaf node is reached
            while cur_node.left_child is not None:
                if input_digits[index] == '0':
                    cur_node = cur_node.left_child
                else:
                    cur_node = cur_node.right_child
                index += 1

            # At a leaf node, collect the symbol
            decode_res += cur_node.item
            cur_node = self.tree_root  # Reset to root for the next symbol

        return decode_res



