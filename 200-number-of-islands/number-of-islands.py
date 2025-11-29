class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m
        
        def dfs(r, c):
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c

                if inbound(nr, nc) and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    dfs(nr, nc) 

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    ans += 1
                    grid[i][j] = '0'
                    dfs(i, j)

        return ans