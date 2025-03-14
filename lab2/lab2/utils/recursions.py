from lab2.NodeClass import TreeNode
from lab2.utils.measures import get_performance


def recur_tree(iterator, char_count=0):
    """
    Build a binary tree for input prefix. Track the number of characters processed.
    :param iterator: the iterator of the input string.
    :param char_count: count for characters processed, starting from 0.
    :return: the root pointer for the binary tree, and the character counts in the input string.
    """

    try:
        item = next(iterator)
        char_count += 1

        if item in {" ", "\n", "\t", "\r", "\xa0"}:  # remove empty and trailing spaces
            item = next(iterator)
            char_count += 1

        root = TreeNode(item)

    except StopIteration:
        raise ValueError("Empty input string")

    if root.type == 'opd':
        return root, char_count

    else:
        root.left_child, char_count = recur_tree(iterator, char_count)
        root.left_child.parent = root

        root.right_child, char_count = recur_tree(iterator, char_count)
        root.right_child.parent = root

    return root, char_count


@get_performance
def recur_conversion(node, to_mode = 'post'):

    """
    Given the binary tree for the input prefix, traverse the tree
    and return the postfix expression of the input
    :param node: the root node of the binary tree
    :param to_mode: which expression to return based on the tree, pre, in, or post
    :return: postfix expression
    """

    if node.type == 'opd':
        return node.item
    else:
        left_opd = recur_conversion(node.left_child, to_mode)
        right_opd = recur_conversion(node.right_child, to_mode)

        # when @get_performance is applied, function returns a tuple
        # extract the postfix (first item in tuple)
        if isinstance(left_opd, tuple):
            left_opd = left_opd[0]
        if isinstance(right_opd, tuple):
            right_opd = right_opd[0]

        # determine the return expression based on the to_mode parameter
        if to_mode == 'post':
            new = left_opd + right_opd + node.item
        elif to_mode == 'pre':
            new = node.item + left_opd + right_opd
        elif to_mode == 'in':
            new = "(" + left_opd + node.item + right_opd + ")"

        return new



