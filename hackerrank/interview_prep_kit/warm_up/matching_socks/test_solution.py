import unittest
from hackerrank.interview_prep_kit.warm_up.matching_socks.solution import sockMerchant

class TestSockMerchant(unittest.TestCase):

    def test_get_one(self):
        self.assertEqual(0, sockMerchant(1, [1]))

    def test_single_pair(self):
        self.assertEqual(1, sockMerchant(2, [2, 2]))

    def test_no_pairs(self):
        self.assertEqual(0, sockMerchant(2, [1, 2]))

    def test_pairs(self):
        self.assertEqual(2, sockMerchant(6, [1, 2, 3, 3, 1, 0]))