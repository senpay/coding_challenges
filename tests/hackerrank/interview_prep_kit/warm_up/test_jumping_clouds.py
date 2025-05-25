import unittest
import hackerrank
import hackerrank.interview_prep_kit
import hackerrank.interview_prep_kit.warm_up
import hackerrank.interview_prep_kit.warm_up.jumping_clouds

from hackerrank.interview_prep_kit.warm_up.jumping_clouds.solution import jumpingOnClouds

class TestJumpingOnClouds(unittest.TestCase):

    def test_double_single_jump(self):
        self.assertEquals(1, jumpingOnClouds([0, 0]))

    def test_double_jump(self):
        self.assertEquals(1, jumpingOnClouds([0, 1]))

    def test_test_safe_cloud_sequence(self):
        self.assertEquals(4, jumpingOnClouds([0, 0, 0, 0, 0, 0, 0]))
        self.assertEquals(3, jumpingOnClouds([0, 0, 0, 0, 0, 0]))

    def test_test_alternating_cloud_sequence(self):
        self.assertEquals(4, jumpingOnClouds([0, 1, 0, 0, 0, 1, 0]))
        self.assertEquals(4, jumpingOnClouds([0, 0, 1, 0, 0, 1]))