class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = []

        @cache
        def dfs(i, j):
            if i == n or j == m or grid[i][j] == 1:
                return 0

            if i == n - 1 and j == m - 1:
                return int(grid[i][j] == 0)

            return dfs(i + 1, j) + dfs(i, j + 1)

        return dfs(0, 0)
