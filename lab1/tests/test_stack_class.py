import unittest
from lab1.stack import Stack


class TestStackClass(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_pop(self):
        self.stack.push("A")
        self.stack.push("B")

        item1 = self.stack.pop()
        item2 = self.stack.pop()

        self.assertTrue(item1 == "B")
        self.assertTrue(item2 == "A")

        # test for error raised when popping empty stack
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push("A")
        self.assertFalse(self.stack.is_empty())


if __name__ == '__main__':
    unittest.main()
