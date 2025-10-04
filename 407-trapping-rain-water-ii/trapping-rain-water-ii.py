class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n, m = len(heightMap), len(heightMap[0])

        if n < 3 or m < 3: return 0

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        queue = []

        for i in range(1, m - 1):
            queue.append((heightMap[0][i], 0, i))
            queue.append((heightMap[-1][i], n - 1, i))

        for i in range(n):
            queue.append((heightMap[i][0], i, 0))
            queue.append((heightMap[i][-1], i, m - 1))

        def inbounds(r, c):
            return 0 <= r < n and 0 <= c < m

        heapify(queue)
        vis = set([(x[1], x[2]) for x in queue])
        ans = 0
        while queue:
            curr, r, c = heappop(queue)
            vis.add((r, c))

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if inbounds(nr, nc) and (nr, nc) not in vis:
                    ans += max(0, curr - heightMap[nr][nc])
                    heappush(queue, (max(curr, heightMap[nr][nc]), nr, nc))
                    vis.add((nr, nc))

        return ans 




