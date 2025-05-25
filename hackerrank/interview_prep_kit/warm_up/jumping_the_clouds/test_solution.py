import unittest
from hackerrank.interview_prep_kit.warm_up.jumping_the_clouds.solution import repeatedString

class TestRepeatedString(unittest.TestCase):

    def test_get_number_from_non_repeated_string(self):
        self.assertEquals(1, repeatedString("asc", 3))

    def test_get_number_from_non_repeated_substring(self):
        self.assertEquals(1, repeatedString("sac", 2))

    def test_dont_miss_first_a(self):
        self.assertEquals(1, repeatedString("asc", 1))

    def test_get_number_from_repeated_string(self):
        self.assertEquals(3, repeatedString("asc", 7))