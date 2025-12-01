class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        queue = deque()

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m

        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        ans = -1
        while queue:
            l = len(queue)

            for _ in range(l):
                r, c = queue.popleft()

                for dr, dc in dirs:
                    nr, nc = dr + r,  c + dc

                    if inbound(nr, nc) and grid[nr][nc]==1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

            ans += 1
        return max(0, ans) if fresh == 0 else -1

        