import unittest

from leetcode.course_schedule.solution import Solution

class TestCourseSchedule(unittest.TestCase):

    def setUp(self):
        self._sut = Solution()
        return super().setUp()
    
    def test_single_course(self):
        self.assertEqual(True, self._sut.canFinish(1, [[]]))

    def test_two_elements(self):
        self.assertEqual(True, self._sut.canFinish(2, [[1, 0]]))
        self.assertEqual(False, self._sut.canFinish(2, [[1,0],[0,1]]))

    def test_complex_graph_no_loop(self):
        self.assertEqual(True, self._sut.canFinish(2, [[1, 0], [3, 0], [3, 1]]))
        self.assertEqual(True, self._sut.canFinish(2, [[2,0],[1,0],[3,1],[3,2]]))
        self.assertEqual(True, self._sut.canFinish(2, [[1,4],[2,4],[3,1],[3,2]]))

    def test_complex_graph_with_loop(self):
        self.assertEqual(False, self._sut.canFinish(2, [[1, 0], [3, 0], [3, 1], [4, 3], [1, 2], [2, 4]]))


    def test_self_dependency(self):
        self.assertEqual(False, self._sut.canFinish(2, [[1,2],[2,3],[3,1]]))
        self.assertEqual(False, self._sut.canFinish(2, [[0,10],[3,18],[5,5],[6,11]]))

    def test_complex_case(self):
        self.assertEqual(False, self._sut.canFinish(2, [[2,0],[1,0],[3,1],[3,2],[1,3]]))

    def test_complex_case_1(self):
        self.assertEqual(False, self._sut.canFinish(2, [[1,0],[2,6],[1,7],[6,4],[7,0]]))
