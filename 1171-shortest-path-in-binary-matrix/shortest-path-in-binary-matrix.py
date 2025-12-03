class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

        if grid[0][0] == 1: return -1

        queue = deque([(0, 0, 1, 1)])
        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m

        while queue:
            r, c, tot, state = queue.popleft()

            if r == n - 1 and c == m - 1:
                return tot

            if state == 1:
                for dr, dc in dirs:
                    nr, nc = r + dr, dc + c

                    if inbound(nr, nc) and grid[nr][nc] == 0:
                        grid[nr][nc] = 1 
                        queue.append((nr, nc, tot + 1, 1))
                queue.append((r, c, tot, 2))
            else:
                grid[r][c] = 0

        return -1
