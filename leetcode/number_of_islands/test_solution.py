import unittest

from leetcode.number_of_islands.solution import Solution

class TestNumberOfIslands(unittest.TestCase):

    def setUp(self):
        self._sut = Solution()
        return super().setUp()

    def test_simple_single_island(self):
        self.assertEquals(1, self._sut.numIslands([['1']]))

    def test_simple_single_vertical_island(self):
        grid = [
            ['0', '0', '0'],
            ['0', '1', '0'],
            ['0', '1', '0']
        ]
        self.assertEquals(1, self._sut.numIslands(grid))

    def test_simple_single_horizontal_island(self):
        grid = [
            ['0', '0', '0', '0'],
            ['0', '1', '1', '0'],
            ['0', '0', '0', '0']
        ]
        self.assertEquals(1, self._sut.numIslands(grid))

    def test_complex_case(self):
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        self.assertEquals(3, self._sut.numIslands(grid))

    def test_complex_shape_island(self):
        grid = [
            ["1","1","1"],
            ["0","1","0"],
            ["1","1","1"]
        ]
        self.assertEquals(1, self._sut.numIslands(grid))

    def test_complex_shape_island_2(self):
        grid = [
            ["1","0","1","1","1"],
            ["1","0","1","0","1"],
            ["1","1","1","0","1"]
        ]
        self.assertEquals(1, self._sut.numIslands(grid))

