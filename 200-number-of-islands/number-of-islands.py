class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n, m = len(grid), len(grid[0])
        ans = 0

        def inbounds(r, c):
            return 0 <= r < n and 0 <= c < m

        def coverIsland(i, j):
            queue = deque([(i, j)])
            grid[i][j] = '0'

            while queue:
                r, c = queue.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if inbounds(nr, nc) and grid[nr][nc] == '1':
                        queue.append((nr, nc))
                        grid[nr][nc] = '0'

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    coverIsland(i, j)
                    ans += 1

        return ans