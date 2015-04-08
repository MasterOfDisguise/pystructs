import unittest

#each fibonacci number is equal to the sum of the previous two
#0 + 1 = 1
#1 + 1 = 2
#1 + 2 = 3
#2 + 3 = 5
#3 + 5 = 8
#5 + 8 = 13

#you are not allowed to use a loop!
#you may use 'if' and 'elif' and 'else'

#def fibonacci(n):
#


class TestFibonacci(unittest.TestCase):

    def test_fib(self):
        self.assertEquals(fibonacci(-2), 0)
        self.assertEquals(fibonacci(-1), 0)
        self.assertEquals(fibonacci(0), 0)
        self.assertEquals(fibonacci(1), 1)
        self.assertEquals(fibonacci(2), 1)
        self.assertEquals(fibonacci(3), 2)
        self.assertEquals(fibonacci(4), 3)
        self.assertEquals(fibonacci(5), 5)
        self.assertEquals(fibonacci(6), 8)
        self.assertEquals(fibonacci(7), 13)
        self.assertEquals(fibonacci(8), 21)
        self.assertEquals(fibonacci(9), 34)