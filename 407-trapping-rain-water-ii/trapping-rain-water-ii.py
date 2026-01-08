class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n, m = len(heightMap), len(heightMap[0])

        if n < 3 or m < 3:
            return 0

        def inbounds(r, c):
            return 0 <= r < n and 0 <= c < m

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        vis = [[False] * m for _ in range(n)]
        queue = []
        ans = 0

        for i in range(1, m - 1):
            heappush(queue, (heightMap[0][i], 0, i))
            heappush(queue, (heightMap[-1][i], n - 1, i))
            vis[0][i] = vis[-1][i] = True

        for i in range(n):
            heappush(queue, (heightMap[i][0], i, 0))
            heappush(queue, (heightMap[i][-1], i, m - 1))
            vis[i][0] = vis[i][-1] = True

        while queue:
            curr, r, c = heappop(queue)

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if inbounds(nr, nc) and not vis[nr][nc]:
                    ans += max(0, curr - heightMap[nr][nc])
                    heappush(queue, (max(curr, heightMap[nr][nc]), nr, nc))
                    vis[nr][nc] = True
        
        return ans

        

