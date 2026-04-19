class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        q = [(0, -sources[i][2], sources[i][0], sources[i][1]) for i in range(len(sources))]
        heapify(q)
        grid = [[0] * m for _ in range(n)]

        for r, c, v in sources:
            grid[r][c] = v

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        curr = 1
        while q:
            for _ in range(len(q)):
                _, v, i, j = heappop(q)

                for dr, dc in dirs:
                    nr, nc = i + dr, j + dc

                    if inbound(nr, nc) and grid[nr][nc] == 0:
                        grid[nr][nc] = -v
                        heappush(q, (curr, v, nr, nc))
            curr += 1

        return grid

