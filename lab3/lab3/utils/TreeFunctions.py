# helper funcitons to read and traverse the trees

from lab3.utils.PriorityListClass import PriorityArray
from lab3.utils.NodeClass import TreeNode


def preorder_traverse(node) -> str:
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

