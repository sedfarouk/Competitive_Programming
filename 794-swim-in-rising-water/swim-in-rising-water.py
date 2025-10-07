class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(0, 1), (-1, 0), (1, 0), (0, -1)]
        vis = set()
        heap = [(grid[0][0], 0, 0)]

        def inbounds(r, c):
            return 0 <= r < n and 0 <= c < m

        while heap:
            mx, i, j = heappop(heap)

            if i == n - 1 and j == m - 1:
                return mx

            for dr, dc in dirs:
                nr, nc = i + dr, j + dc

                if inbounds(nr, nc) and (nr, nc) not in vis:
                    heappush(heap, (max(mx, grid[nr][nc]), nr, nc))
                    vis.add((nr, nc))