class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            grid[r][c] = 0
            for x, y in dirs:
                newr, newc = r+x, c+y
                if 0<=newr<m and 0<=newc<n and grid[newr][newc]:
                    dfs(newr, newc)

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i==0 or j==0 or i==m-1 or j==n-1):
                    dfs(i, j)

        return sum(sum(r) for r in grid)
            