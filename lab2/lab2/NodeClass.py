# This module contains the class for the Node instances of the binary tree,
# implemented as a linked list


class TreeNode:

    def __init__(self, char):
        self.item = char
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.type = self._get_char_type()

    def _get_char_type(self):
        if self.item == "^":
            self.item = "$"
        if self.item.isalpha():
            return 'opd'
        elif self.item in {"/", "*", "$", "+", "-"}:
            return 'op'
        else:
            raise ValueError("Error: wrong input char")

