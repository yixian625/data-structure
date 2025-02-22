# This module provides helper functions for processing and cleaning input strings.
# It includes functions to strip unnecessary whitespace, extract multi-digit numbers,
# and classify characters into operands or operators.

from lab1.stack import Stack


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

    to_strip_set = {"\n", "\t", "\r", "\xa0"}

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


def gather_digits(char: str, line_stack: Stack) -> tuple[str, Stack]:
    """
    Gather all the digits in a number. All digits next to each other are considered to form
    one number. Extract all the digits from the line_stack.
    :param char: the character being processed.
    :param line_stack: the stack used to help process the characters from right to left.
    :return: the number with all its digits; the updated line_stack after all the digits are extracted.
    """

    while line_stack.peek().isdigit():
        char = line_stack.pop() + char

    # separate the number with others with a space at the end
    char = char + " "

    return char, line_stack


def get_char_type(char: str) -> str:
    """
    Determines whether the input character is an operand ("opd")
    or an operator ("op")
    :param char: input character
    :return: "opd" if char is an operand, "op" if it is an operator
    """

    operator_set = {'+', '-', '*', '/', '$'}

    if char.isalpha() or char.isdigit():
        return "opd"

    elif char in operator_set:
        return 'op'

    else:
        raise ValueError("One or more illegal characters in the input string. "
                         "Only letters and +,-,*,/,$,^ are allowed.")
