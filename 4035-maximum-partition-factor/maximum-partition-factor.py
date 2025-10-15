class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [[0] * n for _ in range(n)]
        l = r = 0

        if n == 2:
            return 0

        for i in range(n):
            for j in range(n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dist[i][j] = d
                r = max(r, d)

        def partition(m):
            cols = [-1] * n

            def dfs(u):
                for v in range(n):
                    if u == v: continue

                    if dist[u][v] < m:
                        if cols[v] == -1:
                            cols[v] = 1 - cols[u]

                            if not dfs(v): return False
                        elif cols[u] == cols[v]:
                            return False
                return True

            for u in range(n):
                if cols[u] == -1:
                    cols[u] = 1

                    if not dfs(u): return False
            return True

        ans = 0
        while l <= r:
            m = l + (r - l) // 2

            if partition(m):
                ans = m
                l = m + 1
            else:
                r = m - 1

        return ans

        
                