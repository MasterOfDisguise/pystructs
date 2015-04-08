import unittest

#A stack is like a can of pringles - last in, first out (LIFO)
#You 'push' things to the top of the stack,
#then 'pop' them from the top of the stack.
class Stack(object):
    def __init__(self):
        print('new')


class TestStack(unittest.TestCase):

    def test_new_stack_is_empty(self):
        my_stack = Stack()
        #len(my_stack) calls my_stack.__len__()
        self.assertEquals(len(my_stack), 0)

    def test_can_add_one_thing_to_stack(self):
        my_stack = Stack()
        my_stack.push('a')
        self.assertEquals(len(my_stack), 1)

    def test_can_add_many_things_to_stack(self):
        my_stack = Stack()
        my_stack.push('a')
        my_stack.push('b')
        my_stack.push('c')
        my_stack.push('d')
        self.assertEquals(len(my_stack), 4)

    def test_can_remove_item_from_stack(self):
        my_stack = Stack()
        my_stack.push('a')
        my_stack.push('b')
        my_stack.push('c')
        my_stack.push('d')

        popped = my_stack.pop()
        self.assertEquals(len(my_stack), 3)
        self.assertEquals(popped, 'd')

        popped = my_stack.pop()
        self.assertEquals(len(my_stack), 2)
        self.assertEquals(popped, 'c')

        popped = my_stack.pop()
        self.assertEquals(len(my_stack), 1)
        self.assertEquals(popped, 'b')

        popped = my_stack.pop()
        self.assertEquals(len(my_stack), 0)
        self.assertEquals(popped, 'a')

    def test_can_add_and_remove_from_stack(self):
        my_stack = Stack()
        my_stack.push('a')
        my_stack.push('b')
        my_stack.push('c')
        my_stack.push('d')

        self.assertEquals(my_stack.pop(), 'd')

        my_stack.push('e')
        my_stack.push('f')

        self.assertEquals(my_stack.pop(), 'f')
        self.assertEquals(my_stack.pop(), 'e')

        my_stack.push('g')

        self.assertEquals(my_stack.pop(), 'g')
        self.assertEquals(my_stack.pop(), 'c')
        self.assertEquals(my_stack.pop(), 'b')
        self.assertEquals(my_stack.pop(), 'a')