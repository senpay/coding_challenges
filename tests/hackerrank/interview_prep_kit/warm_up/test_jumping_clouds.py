import unittest
from hackerrank.interview_prep_kit.warm_up.jumping_clouds.solution import jumpingOnClouds

class TestJumpingOnClouds(unittest.TestCase):

    def test_get_number_from_non_repeated_string(self):
        self.assertEquals(1, jumpingOnClouds([0, 0]))
