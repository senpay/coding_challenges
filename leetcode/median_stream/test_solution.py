import unittest
from median_stream.solution import MedianFinder

class TestMedianFinder(unittest.TestCase):

    def setUp(self):
        self._sut = MedianFinder()
        return super().setUp()


    def test_get_single(self):
        self._sut.addNum(2)
        self.assertEquals(2, self._sut.findMedian())

    def test_get_two(self):
        self._sut.addNum(3)
        self._sut.addNum(2)
        self.assertEquals(2.5, self._sut.findMedian())

    def test_get_three(self):
        self._sut.addNum(2)
        self._sut.addNum(3)
        self._sut.addNum(-1)
        self.assertEquals(2, self._sut.findMedian())

    def test_get_four(self):
        self._sut.addNum(2)
        self._sut.addNum(3)
        self._sut.addNum(-1)
        self._sut.addNum(10)
        self.assertEquals(2.5, self._sut.findMedian())

    def test_add_check_tree_balance(self):
        self._sut.addNum(6)
        self._sut.addNum(10)
        self._sut.addNum(2)
        self._sut.addNum(6)
        self._sut.addNum(5)
        self._sut.addNum(0)
 
        self.assertEquals(5.5, self._sut.findMedian())       


    def test_add_failing_from_leetcode(self):
        self._sut.addNum(1)
        self._sut.addNum(2)
        self._sut.addNum(3)
        self._sut.addNum(4)


 
        self.assertEquals(2.5, self._sut.findMedian())    
