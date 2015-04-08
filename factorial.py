import unittest

#factorial(5) = 5 * 4 * 3 * 2 * 1

#you are not allowed to use a loop!
#you may use 'if' and 'elif' and 'else'

#def factorial(n):
#


class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        self.assertEquals(factorial(0), 1)
        self.assertEquals(factorial(1), 1)
        self.assertEquals(factorial(2), 2)
        self.assertEquals(factorial(3), 6)
        self.assertEquals(factorial(4), 24)
        self.assertEquals(factorial(5), 120)
        self.assertEquals(factorial(6), 720)