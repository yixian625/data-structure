# module containing the node class for linked list


class Node:

    def __init__(self, value):
        self.data = value
        self.next = None

    def __repr__(self):
        return f'Node: data {self.data}, pointing to {self.next}'


