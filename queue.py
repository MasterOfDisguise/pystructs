import unittest

#A queue is like a line at the grocery store - first in, first out (FIFO)
#You 'enqueue' things to the back of the queue,
#then 'dequeue' them from the front of the queue.
class Queue(object):
    def __init__(self):
        print('new')


class TestQueue(unittest.TestCase):

    def test_new_queue_is_empty(self):
        my_queue = Queue()
        #len(my_queue) calls my_queue.__len__()
        self.assertEquals(len(my_queue), 0)

    def test_can_add_one_thing_to_queue(self):
        my_queue = Queue()
        my_queue.enqueue('a')
        self.assertEquals(len(my_queue), 1)

    def test_can_add_many_things_to_queue(self):
        my_queue = Queue()
        my_queue.enqueue('a')
        my_queue.enqueue('b')
        my_queue.enqueue('c')
        my_queue.enqueue('d')
        self.assertEquals(len(my_queue), 4)

    def test_can_remove_item_from_queue(self):
        my_queue = Queue()
        my_queue.enqueue('a')
        my_queue.enqueue('b')
        my_queue.enqueue('c')
        my_queue.enqueue('d')

        front = my_queue.dequeue()
        self.assertEquals(len(my_queue), 3)
        self.assertEquals(front, 'a')

        front = my_queue.dequeue()
        self.assertEquals(len(my_queue), 2)
        self.assertEquals(front, 'b')

        front = my_queue.dequeue()
        self.assertEquals(len(my_queue), 1)
        self.assertEquals(front, 'c')

        front = my_queue.dequeue()
        self.assertEquals(len(my_queue), 0)
        self.assertEquals(front, 'd')

    def test_can_add_and_remove_from_queue(self):
        my_queue = Queue()
        my_queue.enqueue('a')
        my_queue.enqueue('b')
        my_queue.enqueue('c')
        my_queue.enqueue('d')

        self.assertEquals(my_queue.dequeue(), 'a')

        my_queue.enqueue('e')
        my_queue.enqueue('f')

        self.assertEquals(my_queue.dequeue(), 'b')
        self.assertEquals(my_queue.dequeue(), 'c')

        my_queue.enqueue('g')

        self.assertEquals(my_queue.dequeue(), 'd')
        self.assertEquals(my_queue.dequeue(), 'e')
        self.assertEquals(my_queue.dequeue(), 'f')
        self.assertEquals(my_queue.dequeue(), 'g')