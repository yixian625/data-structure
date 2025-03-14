# print("a".isalpha())
#
# print("A" + "ABC+" + "/")
#
# # with open("resources/input/Required-Input.txt", 'r') as file:
# #     for line in file:
# #         for char in line:
# #             print(repr(char))
# print("112 ".isdigit())


prefix = "-+XABC/EF"


class TreeNode:

    def __init__(self, char):
        self.item = char
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.type = self._get_char_type()

    def _get_char_type(self):
        if self.item.is_alpha() or self.item.is_digit():
            self.type = 'opd'
        elif self.item in {"/", "*", "^", "$", "+", "-"}:
            self.type = 'op'
        else:
            raise ValueError("wrong input char")


def recur_tree(input_string):

    root = TreeNode(input_string[0])

    if root.type == 'opd':
        return root.item

    else:
        root.left_child = recur_tree(next(input_string))
        root.right_child = recur_tree(next(input_string))

    return root

