import unittest

from leetcode.sub_ar_sum.solution import Solution

class TestSubArSum(unittest.TestCase):

    def setUp(self):
        self._sut = Solution()
        return super().setUp()

    def test_single_element_ar(self):
        self.assertEquals(1, self._sut.subarraySum([2], 2))
        self.assertEquals(0, self._sut.subarraySum([2], 1))

    def test_simple_ar_with_two_sub_ars(self):
        self.assertEquals(2, self._sut.subarraySum([1, 2, 3, 4], 3))
        self.assertEquals(2, self._sut.subarraySum([1, 1, 1], 2))
        self.assertEquals(1, self._sut.subarraySum([1, 1, 3, 4], 3))

    def test_no_fitting_sub_array(self):
        self.assertEquals(0, self._sut.subarraySum([1, 2, 6], 5))
        self.assertEquals(0, self._sut.subarraySum([2, 2, 6], 0))

    def test_negative_numbers(self):
        self.assertEquals(1, self._sut.subarraySum([-1, -1, 1], 0))

    def test_complex_permutations(self):
        self.assertEquals(6, self._sut.subarraySum([0,0,0], 0))
        self.assertEquals(55, self._sut.subarraySum([0,0,0,0,0,0,0,0,0,0], 0))