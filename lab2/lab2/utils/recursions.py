from lab2.NodeClass import TreeNode


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



