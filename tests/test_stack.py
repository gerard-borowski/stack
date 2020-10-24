from unittest import TestCase
from stack import Stack


class TestStackOperations(TestCase):

    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        self.stack.clear()


    def test_should_add_new_element_to_stack(self):
        value, expected = 42, 42

        self.stack.push(value)

        self.assertEqual(self.stack.peek(), expected)

    def test_should_remove_last_element_from_stack(self):
        element, expected = 42, 42
        self.stack.push(element)

        value = self.stack.pop()

        self.assertEqual(value, expected)
        self.assertEqual(self.stack.size, 0)

    # def test_peek_should_show_the_last_element_(self):
    #     element, expected = 42, 42
    #     stack = Stack()
    #     stack.push(element)
    #
    #     value =stack.peek()
    #
    #     self.assertEqual(value, expected)
    #     self.assertEqual(stack, size, 1)
    #
    # def test_should_clear(self):
    #     self.stack.push(42)
    #     self.stack.push(43)
    #

    def test_should_raise_when_called_pop(self):
        self.fail("not implemanted yet")

##gg