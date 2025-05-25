import unittest
from hackerrank.interview_prep_kit.warm_up.counting_valleys.solution import countingValleys

class TestCountingValleys(unittest.TestCase):

    def test_get_zero(self):
        self.assertEqual(0, countingValleys(1, "U"))

    def test_get_one(self):
        self.assertEqual(1, countingValleys(1, "DDU"))

    def test_get_one_very_short(self):
        self.assertEqual(1, countingValleys(1, "DU"))
        self.assertEqual(1, countingValleys(1, "D"))

    def test_get_long_valley(self):
        self.assertEqual(1, countingValleys(1, "UDDDUDUU"))

    def test_get_long_valley_and_one_more(self):
        self.assertEqual(2, countingValleys(1, "UDDDUDUUDDD"))
