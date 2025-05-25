# Very cool graph traversal problem
# see: https://leetcode.com/problems/number-of-islands

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 300
#     grid[i][j] is '0' or '1'.

class Solution(object):

    def explore_island(self, grid, row_index, column_index, visited_nodes):
        if (row_index, column_index) in visited_nodes:
            return
        
        visited_nodes.add((row_index, column_index))

        # explore left
        if not self.is_water(grid, row_index, column_index - 1):
           self.explore_island(grid, row_index, column_index - 1, visited_nodes)

        # explore right
        if not self.is_water(grid, row_index, column_index + 1):
           self.explore_island(grid, row_index, column_index + 1, visited_nodes) 

        # explore down
        if not self.is_water(grid, row_index + 1, column_index):
           self.explore_island(grid, row_index + 1, column_index, visited_nodes)

        # explore up
        if not self.is_water(grid, row_index - 1, column_index):
           self.explore_island(grid, row_index - 1, column_index, visited_nodes)


                
    def is_water(self, grid, row_index, column_index):
        return (
            row_index >= len(grid) or
            row_index < 0 or
            column_index >= len(grid[0]) or
            column_index < 0 or
            grid[row_index][column_index] == '0'      
        )      

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        number_of_islands = 0

        visited_nodes = set()

        for row_index in range(len(grid)):
            for column_index in range(len(grid[0])):

                if self.is_water(grid, row_index, column_index) or (row_index, column_index) in visited_nodes:
                    continue
                else:
                    number_of_islands += 1
                    self.explore_island(grid, row_index, column_index, visited_nodes)

        return number_of_islands

                    

        