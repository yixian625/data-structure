# This module contains a priority class that helps store and sort the nodes based on their priority.
# Sorting is implemented with merge sort.

from lab3.utils.NodeClass import TreeNode


class PriorityArray:

    def __init__(self):
        self.nodes = []

    def __len__(self):
        return len(self.nodes)

    def insert(self, node: TreeNode):
        self.nodes.append(node)

    def pop_first(self):
        if len(self.nodes) == 0:
            raise IndexError("There is no item left in the list to pop.")
        item = self.nodes[0]
        self.nodes = self.nodes[1:]
        return item

    def sort(self):
        self.nodes = self._recursive_merge_sort(self.nodes)

    def _recursive_merge_sort(self, node_list):
        """
        Recursively split the nodes in node_list, sort them,
        then merge back to one sorted list. The nodes that should
        be used first in the huffman tree is put that the beginning of
        the list.
        :param node_list: list of nodes to sort
        :return: sorted list
        """
        # base case:
        if len(node_list) == 1:
            return node_list

        # recursive calls:
        middle = len(node_list)//2
        left = self._recursive_merge_sort(node_list[:middle])
        right = self._recursive_merge_sort(node_list[middle:])

        # resolving ties
        return self._merge(left, right)

    @staticmethod
    def _merge(left, right):
        sorted_list = []
        # start pointers
        i = j = 0

        # merge until one of the subfile is depleted
        while i < len(left) and j < len(right):

            if left[i].freq < right[j].freq:
                sorted_list.append(left[i])
                i += 1

            elif left[i].freq == right[j].freq:

                # prioritize the single-letter group when frequencies are the same
                if len(left[i].item) == 1 and len(right[j].item) > 1:
                    sorted_list.append(left[i])
                    i += 1

                elif len(right[j].item) == 1 and len(left[i].item) > 1:
                    sorted_list.append(right[j])
                    j += 1

                # if both contain single or both contain multiple letters,
                # use the smallest alphabet in the group to solve tie
                else:
                    smallest_left = min(left[i].item)
                    smallest_right = min(right[j].item)
                    if smallest_left < smallest_right:
                        sorted_list.append(left[i])
                        i += 1
                    else:
                        sorted_list.append(right[j])
                        j += 1

            else:
                sorted_list.append(right[j])
                j += 1

        # when either left or right is depleted,
        # add the rest of the other subfile
        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])

        return sorted_list









