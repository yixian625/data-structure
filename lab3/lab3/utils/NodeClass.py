# This module contains the class for the Node instances of the binary tree,
# implemented as a linked list.

class TreeNode:

    def __init__(self, char, freq):
        self.item = char
        self.freq = freq
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return f"Node(item={self.item}, freq={self.freq})"


