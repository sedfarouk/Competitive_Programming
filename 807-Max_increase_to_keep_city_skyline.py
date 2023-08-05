# 807. Leetcode - Max Increase To Keep City Skyline

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0
        cols = list(map(tuple, zip(*grid)))
        col_maxs = [max(i) for i in cols]

        for i in range(len(grid)):
            max_row = max(grid[i])
            for j in range(len(grid[i])):
                max_grid = col_maxs[j]
                min_num = min(max_row, max_grid)
                ans+= min_num - grid[i][j]

        return ans
