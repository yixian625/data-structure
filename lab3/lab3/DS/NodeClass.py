# This module contains the class for the Node instances of the binary tree,

class TreeNode:

    def __init__(self, char, freq):
        self.item = char
        self.freq = freq
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return f"Node(item={self.item}, freq={self.freq})"

    def __add__(self, other):
        new_item = self.item + other.item
        new_freq = self.freq + other.freq
        new_node = TreeNode(new_item, new_freq)
        new_node.left_child = self
        new_node.right_child = other
        return new_node

