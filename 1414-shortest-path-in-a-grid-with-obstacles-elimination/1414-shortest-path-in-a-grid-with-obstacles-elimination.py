class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def inbounds(r, c):
            return 0 <= r < n and 0 <= c < m

        queue = deque([(0, 0, 0, k)])
        visited = set()
        while queue:
            row, col, cnt, q = queue.popleft()
            if row==n-1 and col==m-1:
                return cnt

            if (row, col, q) in visited:
                continue
            visited.add((row, col, q))

            for dr, dc in dirs:
                newr, newc = row + dr, col + dc
                if inbounds(newr, newc):
                    if grid[newr][newc]==0:
                        queue.append((newr, newc, cnt+1, q))

                    elif grid[newr][newc]==1 and q > 0:
                        queue.append((newr, newc, cnt+1, q-1))
        return -1

        