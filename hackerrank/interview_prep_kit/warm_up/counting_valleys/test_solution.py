import unittest
from counting_valleys.solution import countingValleys

class TestCountingValleys(unittest.TestCase):

    def test_get_zero(self):
        self.assertEquals(0, countingValleys(1, "U"))

    def test_get_one(self):
        self.assertEquals(1, countingValleys(1, "DDU"))

    def test_get_one_very_short(self):
        self.assertEquals(1, countingValleys(1, "DU"))
        self.assertEquals(1, countingValleys(1, "D"))

    def test_get_long_valley(self):
        self.assertEquals(1, countingValleys(1, "UDDDUDUU"))

    def test_get_long_valley_and_one_more(self):
        self.assertEquals(2, countingValleys(1, "UDDDUDUUDDD"))
