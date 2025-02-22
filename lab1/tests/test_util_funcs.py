import unittest
from lab1.stack import Stack
from lab1.utils.input_processing import get_char_type
from lab1.utils.stack_operation import process_char_with_stack


class TestStackClass(unittest.TestCase):

    def test_getting_char_type(self):
        self.assertTrue(get_char_type("G") == 'opd')
        self.assertTrue(get_char_type("/") == 'op')

        with self.assertRaises(ValueError):
            get_char_type('%')

    def test_process_char(self):
        cur_stack = Stack()
        cur_stack.push('A')
        cur_stack.push('B')

        updated_stack = process_char_with_stack('/', 'op', cur_stack)
        self.assertTrue(updated_stack.size() == 1)

        updated_stack = process_char_with_stack('A', 'opd', cur_stack)
        self.assertTrue(updated_stack.size() == 2)
        self.assertTrue(updated_stack.pop() == 'A')

    def test_process_char_invalid(self):
        cur_stack = Stack()
        updated_stack = process_char_with_stack('A', 'opd', cur_stack)
        with self.assertRaises(IndexError):
            process_char_with_stack('-', 'op', updated_stack)


if __name__ == '__main__':
    unittest.main()
