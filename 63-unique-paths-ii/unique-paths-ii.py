class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dirs = [(1, 0), (0, 1)]

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m

        @cache
        def dp(r, c):
            if obstacleGrid[r][c]:
                return 0
                
            if r == n - 1 and c == m - 1:
                return 1

            ans = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if inbound(nr, nc):
                    ans += dp(nr, nc)

            return ans

        res = dp(0, 0)
        dp.cache_clear()
        return res