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

        def dfs(r, c, vis):
            ans = 0
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c

                if (nr, nc) not in vis and inbounds(nr, nc):
                    if grid[nr][nc] == 2:
                        ans += len(vis) == p
                    elif not grid[nr][nc]:
                        ans += dfs(nr, nc, vis.union(set([(nr, nc)])))
            return ans

        return dfs(x, y, set())

            
        