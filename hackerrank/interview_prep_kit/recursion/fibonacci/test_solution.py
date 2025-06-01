import unittest

from hackerrank.interview_prep_kit.recursion.fibonacci.solution import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_zero(self):
        self.assertEquals(fibonacci(0), 0)

    def test_fibonacci_one(self):
        self.assertEquals(fibonacci(1), 1)

    def test_fibonacci_three(self):
        self.assertEquals(fibonacci(6), 8) 

    def test_fibonacci(self):
        self.assertEquals(fibonacci(100), 354224848179261915075)
