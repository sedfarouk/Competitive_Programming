class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        if grid[0][0] != 0:
            return -1

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)]

        def inbounds(r, c):
            return 0 <= r < n and 0 <= c < m

        queue = deque([(0, 0, 1)])
        grid[0][0] = 1

        while queue:
            r, c, steps = queue.popleft()

            if r == n - 1 and c == m - 1:
                return steps

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if inbounds(nr, nc) and grid[nr][nc] == 0:
                    queue.append((nr, nc, steps + 1))
                    grid[nr][nc] = 1

        return -1
