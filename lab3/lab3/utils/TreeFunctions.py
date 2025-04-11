# helper funcitons to read and traverse the trees

from lab3.utils.PriorityListClass import PriorityArray
from lab3.utils.NodeClass import TreeNode


def preorder_traverse(node: TreeNode) -> str:
    """
    Takes the root node of the Huffman encoding tree and print
    out the encoding with recursive calls.
    :param node:
    :return:
    """
    # base case -
    # strict binary tree, if no left_child, there's no right child either
    if node.left_child is None:
        return f"{node.item}:{node.freq} "
    else:
        left_tree = preorder_traverse(node.left_child)
        right_tree = preorder_traverse(node.right_child)
        sub_tree = f"{node.item}:{node.freq} " + left_tree + right_tree

        return sub_tree


def get_letter_code(node, char) -> str:
    """
    Takes the root node of a tree, traverse the tree to find
    the input character, return the Huffman code for that
    character
    :param node: root node of the Huffman encoding tree
    :param char: character to get the code for
    :return: the Huffman code for that character
    """

    cur_node = node
    char_code = ''
    while cur_node.left_child is not None:
        if char in cur_node.left_child.item:
            char_code = char_code + '0'
            cur_node = cur_node.left_child
        else:
            char_code = char_code + '1'
            cur_node = cur_node.right_child

    return char_code


def get_decoded_letter(node, input_digits) -> str:
    """
    Takes the root node of a Huffman encoding tree and a string
    of digits. Traverse the tree based on the digits and return
    the decoded message
    :param node: root node of a Huffman encoding tree
    :param input_digits: encrypted message in the form of a string of digits
    :return: the decoded message in alphabets
    """
    cur_node = node
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
        cur_node = node  # Reset to root for the next symbol

    return decode_res



