# This module contains recursive functions to build the tree,
# traverse the tree, and count the number of nodes int the tree.
from lab2.NodeClass import TreeNode


def recur_tree(iterator):
    """
    Build a binary tree for input prefix. Track the number of characters processed.
    :param iterator: the iterator of the input string.
    :return: the root pointer for the binary tree, and the character counts in the input string.
    """

    try:
        item = next(iterator)

        if item in {" ", "\n", "\t", "\r", "\xa0"}:  # remove empty and trailing spaces
            item = next(iterator)

        root = TreeNode(item)

    except StopIteration:
        raise ValueError("Error: too many operators.")

    if root.type == 'opd':
        return root

    else:
        root.left_child = recur_tree(iterator)
        root.left_child.parent = root

        root.right_child = recur_tree(iterator)
        root.right_child.parent = root

    return root


def recur_conversion(node, to_mode='post'):

    """
    Given the binary tree for the input prefix, traverse the tree
    and return the postfix expression of the input
    :param node: the root node of the binary tree
    :param to_mode: which expression to return based on the tree: in, or post
    :return: postfix expression
    """

    if node.type == 'opd':
        return node.item
    else:
        left_opd = recur_conversion(node.left_child, to_mode)
        right_opd = recur_conversion(node.right_child, to_mode)

        # determine the return expression based on the to_mode parameter
        if to_mode == 'post':
            new = left_opd + right_opd + node.item
        elif to_mode == 'pre':
            new = node.item + left_opd + right_opd
        elif to_mode == 'in':
            new = "(" + left_opd + node.item + right_opd + ")"

        return new


def recur_get_num_nodes(root, count=0):

    """
    Counts the number of nodes in the tree by recursively following
    the left and child pointers.
    :param root: the root node of a tree
    :param count: count tracking, starting from 0
    :return: the total number of nodes in a tree
    """

    count += 1

    # the binary tree must be complete so if there's no
    # left child, it must be a leaf
    if root.left_child is None:
        return count

    else:
        count = recur_get_num_nodes(root.left_child, count)
        count = recur_get_num_nodes(root.right_child, count)

    return count





