import unittest


class List(object):
    def __init__(self):
        self.head = None
        print('new')

    def append(self, value):
        end_node = self.head
        new_node = Node(value)
        if self.head is None:
            self.head = Node(value)
        elif self.head is not None:
            while end_node.next is not None:
                end_node = end_node.next
            end_node.next = new_node

    def __len__(self):
        len = 0
        if self.head is None:
            return len
        elif self.head is not None:
            true = True
            target = self.head
            len += 1
            while true:
                if target.next is None:
                    true = False
                    return len
                target = target.next
                len += 1

    def __getitem__(self, item):
        target = self.head
        if item > len(self):
            print "Error, item does not exist"
        elif item <= len(self):
            for i in range(item):
                target = self.head.next
            return target.value


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class TestList(unittest.TestCase):

    def test_new_list_is_empty(self):
        my_list = List()
        #len(my_list) calls my_list.__len__()
        self.assertEquals(len(my_list), 0)

    def test_can_add_one_thing_to_list(self):
        my_list = List()
        my_list.append('a')
        self.assertEquals(len(my_list), 1)
        #my_list[0] calls my_list.__getitem__(0)
        self.assertEquals(my_list[0], 'a')

    def test_can_add_many_things_to_list(self):
        my_list = List()
        my_list.append('a')
        my_list.append('b')
        my_list.append('c')
        my_list.append('d')
        self.assertEquals(len(my_list), 4)
        self.assertEquals(my_list[0], 'a')
        self.assertEquals(my_list[1], 'b')
        self.assertEquals(my_list[2], 'c')
        self.assertEquals(my_list[3], 'd')

    def test_can_insert_into_middle_of_list(self):
        my_list = List()
        my_list.append('a')
        my_list.append('b')
        my_list.append('c')
        my_list.insert(1, 'd') #1 is the index. This should put d at index 1, and shove everything else forward
        self.assertEquals(len(my_list), 4)
        self.assertEquals(my_list[0], 'a')
        self.assertEquals(my_list[1], 'd')
        self.assertEquals(my_list[2], 'b')
        self.assertEquals(my_list[3], 'c')

    def test_can_remove_item_from_list(self):
        my_list = List()
        my_list.append('a')
        my_list.append('b')
        my_list.append('c')
        my_list.append('d')
        my_list.remove('c')
        self.assertEquals(len(my_list), 3)
        self.assertEquals(my_list[0], 'a')
        self.assertEquals(my_list[1], 'b')
        self.assertEquals(my_list[2], 'd')

    def test_can_find_item_in_list(self):
        my_list = List()
        my_list.append('a')
        my_list.append('b')
        my_list.append('c')
        my_list.append('d')
        self.assertEquals(my_list.index('a'), 0)
        self.assertEquals(my_list.index('b'), 1)
        self.assertEquals(my_list.index('c'), 2)
        self.assertEquals(my_list.index('d'), 3)

    def test_can_count_item_in_list(self):
        my_list = List()
        my_list.append('a')
        my_list.append('b')
        my_list.append('c')
        my_list.append('a')
        my_list.append('c')
        my_list.append('d')
        my_list.append('a')
        self.assertEquals(my_list.count('a'), 3)
        self.assertEquals(my_list.count('b'), 1)
        self.assertEquals(my_list.count('c'), 2)
        self.assertEquals(my_list.count('d'), 1)
        self.assertEquals(my_list.count('e'), 0)

    # we'll come back to this one later
    # def test_can_sort_list(self):
    #     my_list = List()
    #     my_list.append('c')
    #     my_list.append('a')
    #     my_list.append('d')
    #     my_list.append('b')
    #     my_list.sort()
    #     self.assertEquals(len(my_list), 4)
    #     self.assertEquals(my_list[0], 'a')
    #     self.assertEquals(my_list[1], 'd')
    #     self.assertEquals(my_list[2], 'b')
    #     self.assertEquals(my_list[3], 'c')

    def test_can_reverse_list(self):
        my_list = List()
        my_list.append('a')
        my_list.append('b')
        my_list.append('c')
        my_list.append('d')
        my_list.reverse()
        self.assertEquals(len(my_list), 4)
        self.assertEquals(my_list[0], 'd')
        self.assertEquals(my_list[1], 'c')
        self.assertEquals(my_list[2], 'b')
        self.assertEquals(my_list[3], 'a')

    def test_can_add_many_kinds_of_things_to_list(self):
        my_list = List()
        my_list.append('a')
        my_list.append(2)
        my_list.append('abcde')
        my_list.append([1, 2, 3])
        self.assertEquals(len(my_list), 4)
        self.assertEquals(my_list[0], 'a')
        self.assertEquals(my_list[1], 2)
        self.assertEquals(my_list[2], 'abcde')
        self.assertEquals(my_list[3], [1, 2, 3])
