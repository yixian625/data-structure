# function to string end-of-line spaces and provide an input character count of the clean line
# uses a stack to manage the process

class Stack:
    def __init__(self):
        """
        This class is used to hold items in a stack.
        """
        self.items = []
        self.len = 0

    def is_empty(self) -> bool:
        """
        Determines if the stack is currently holding any items
        :return: True if the stack currently has no items
        """
        return self.len == 0

    def pop(self) -> str:
        """
        Removes one int from the top of the stack and returns it.
        Stack must not be empty when popping.
        Update item list of the stack and stack length.
        :return: The current item on top of the stack.
        """
        if self.len == 0:
            raise IndexError("Stack is empty. Cannot Pop.")

        item = self.items[-1]
        del self.items[-1]
        self.len = self.len - 1

        return item

    def push(self, new_item: str) -> None:
        """
        Pushes an item on to the stack
        Update item list of the stack and stack length
        :param new_item: the item to insert.
        """
        self.items.append(new_item)
        self.len = self.len + 1


def get_stripped_line(line: str) -> (str | None, int):
    """
    Strip new line and tab characters from the end of each line
    to make output prettier. Keep a count for the number of characters for
    performance measuring.
    :param line: input string
    :return: the trimmed input string and the number of characters in the string
    """
    stack = Stack()
    auxi_stack = Stack()  # for reversing the order

    to_strip_set = {" ", "\n", "\t", "\r", "\xa0"}

    char_count = 0

    for char in line:
        if char in to_strip_set:  # skip new line and tab character
            continue
        else:
            stack.push(char)
            char_count += 1

    if stack.is_empty():
        return None, 0

    # reconstructing the original line,
    # popping + pushing one at time to not use the join method for string
    while not stack.is_empty():
        char = stack.pop()
        if auxi_stack.is_empty():
            auxi_stack.push(char)
        else:
            original = auxi_stack.pop()
            auxi_stack.push(char + original)

    original = auxi_stack.pop()

    return original, char_count
