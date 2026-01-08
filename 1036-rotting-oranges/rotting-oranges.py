class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque()
        ans = fresh = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    grid[i][j] = 0
                
                elif grid[i][j] == 1:
                    fresh += 1

        def inbounds(r, c):
            return 0 <= r < n and 0 <= c < m

        if fresh == 0:
            return 0
        
        while queue:
            l = len(queue)
            old_fresh = fresh

            for _ in range(l):
                r, c = queue.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if inbounds(nr, nc) and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 0
                        queue.append((nr, nc))

            ans += old_fresh != fresh

        return ans if fresh == 0 else -1