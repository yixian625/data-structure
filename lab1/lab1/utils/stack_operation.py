# This module provides helper functions for manipulating stacks in the
# prefix-to-postfix conversion process. It ensures proper handling of
# operands and operators.

from lab1.stack import Stack


def process_char_with_stack(char: str,
                            char_type: str,
                            cur_stack: Stack) -> Stack:
    """
    Process an input character based on its type.
    If it's an operand, push it to the current stack;
    if it's an operator, pop from the stack twice,
    combine the popped operands and the operator,
    push the combined item back to stack.
    Return the updated stack

    :param char: input character
    :param char_type: 'op' if operator, 'opd' if operand
    :param cur_stack: current stack
    :return: updated stack
    """

    if char_type == 'opd':
        cur_stack.push(char)

    elif char_type == 'op':
        try:
            item1 = cur_stack.pop()
            item2 = cur_stack.pop()
        except IndexError:
            raise IndexError("Input prefix is invalid. Too many operators.")
        else:
            new_item = item1 + item2 + char
            cur_stack.push(new_item)

    return cur_stack
