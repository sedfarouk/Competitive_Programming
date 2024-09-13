class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        if k>=m+n-2:
            return m+n-2 

        def inbounds(r, c):
            return 0 <= r < n and 0 <= c < m

        queue = deque([(0, 0, k)])
        visited = set((0, 0, k))
        cnt = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                row, col, q = queue.popleft()
                if row==n-1 and col==m-1:
                    return cnt

                for dr, dc in dirs:
                    newr, newc = row + dr, col + dc
                    if inbounds(newr, newc):
                        if grid[newr][newc]==0 and (newr, newc, q) not in visited:
                            queue.append((newr, newc, q))
                            visited.add((newr, newc, q))

                        elif grid[newr][newc]==1 and q > 0 and (newr, newc, q-1) not in visited:
                            queue.append((newr, newc, q-1))
                            visited.add((newr, newc, q-1))
            cnt += 1
        return -1

        