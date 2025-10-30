class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        x = y = p = 0

        for i in range(n):
            for j in range(m):
                p += grid[i][j] == 0
                if grid[i][j] == 1:
                    x, y = i, j

        dirs = [(0, 1), (1, 0), (-1, 0),(0, -1)]

        def inbounds(r, c):
            return 0 <= r < n and 0 <= c < m

        def dfs(r, c, p):
            ans = 0
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c

                if inbounds(nr, nc) and grid[nr][nc] != -1:
                    if grid[nr][nc] == 2:
                        ans += not p
                    elif not grid[nr][nc]:
                        grid[nr][nc] = -1
                        ans += dfs(nr, nc, p - 1)
                        grid[nr][nc] = 0
            return ans

        return dfs(x, y, p)

            
        