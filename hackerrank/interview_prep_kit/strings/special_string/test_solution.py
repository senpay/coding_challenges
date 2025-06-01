import unittest

from hackerrank.interview_prep_kit.strings.special_string.solution import substrCount, is_special_string


class TestSubstringCount(unittest.TestCase):

    def test_common_simple_strings(self):
        self.assertEqual(is_special_string("a"), True)
        self.assertEqual(is_special_string("aa"), True)
        self.assertEqual(is_special_string("aaa"), True)
        self.assertEqual(is_special_string("ada"), True)
        self.assertEqual(is_special_string("aadaa"), True)

    def test_negative_common_simple_strings(self):
        self.assertEqual(is_special_string("ab"), False)
        self.assertEqual(is_special_string("abb"), False)
        self.assertEqual(is_special_string("abb"), False)

    def test_single_char_and_empty_string(self):
        self.assertEqual(substrCount(1, "a"), 1)
        self.assertEqual(substrCount(0, ""), 0)

    def test_simple_case_triple_a_string(self):
        self.assertEqual(substrCount(3, "aaa"), 6)

    def test_less_simple_string(self):
        self.assertEqual(substrCount(3, "ada"), 4)
        self.assertEqual(substrCount(3, "add"), 4)

    def test_example_string(self):
        self.assertEqual(substrCount(9, "mnonopoo"), 12)



