import unittest

from leetcode.top_k_frequent_elements.solution import Solution

class TestKFreqElements(unittest.TestCase):

    def setUp(self):
        self._sut = Solution()
        return super().setUp()

    def test_request_all_elements(self):
        self.assertEquals([1], self._sut.topKFrequent([1], 1))
        self.assertEquals([1, 2], self._sut.topKFrequent([1, 2, 1], 2))
        self.assertEquals([1, 2], self._sut.topKFrequent([1, 2], 2))


    def test_request_single_most_frequent(self):
        self.assertEquals([1], self._sut.topKFrequent([1], 1))
        self.assertEquals([1], self._sut.topKFrequent([1, 2, 1], 1))
        self.assertEquals([1], self._sut.topKFrequent([1, 2], 1))

    def test_leetcode_example(self):
        self.assertEquals([1, 2], self._sut.topKFrequent([1,1,1,2,2,3], 2))
        self.assertEquals([1, 2, 3], self._sut.topKFrequent([1,1,1,2,2,3], 3))