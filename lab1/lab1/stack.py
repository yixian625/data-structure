# This module creates the Stack class used in the input processing and
# the conversion functions


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

    def size(self) -> int:
        """
        Determines how many items currently are in the stack.
        :return number of items in stack:
        """
        return self.len

    def peek(self) -> str:
        """
        Show the top item on the stack
        :return top item. Stack remain unchanged
        """
        return self.items[-1]
