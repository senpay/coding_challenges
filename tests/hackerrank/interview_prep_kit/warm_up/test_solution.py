import unittest
from hackerrank.interview_prep_kit.warm_up.jumping_clouds.jumping_clouds import jumpingOnClouds

class TestJumpingOnClouds(unittest.TestCase):

    def test_get_number_from_non_repeated_string(self):
        self.assertEquals(1, jumpingOnClouds([0, 0]))
