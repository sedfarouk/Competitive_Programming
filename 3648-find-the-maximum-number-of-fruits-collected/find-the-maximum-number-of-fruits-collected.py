class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        ans = fruits[-1][0] + fruits[0][-1]

        for i in range(n):
            ans += fruits[i][i]
            fruits[i][i] = 0

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < n

        def canMove(steps, r, c):
            diag = min(n - r - 1, n - c - 1)
            down, right = n - (r + diag) - 1, n - (c + diag) - 1
            totalMoves = steps + diag + down + right + 1
            return totalMoves <= n - 1

        dirs = [(-1, 1), (0, 1), (1, 1), (1, -1), (1, 0)]
        @cache
        def dp(r, c, steps):
            if r == n - 1 and c == n - 1:
                return 0
            
            ans = 0
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c

                if inbound(nr, nc) and canMove(steps, nr, nc):
                    ans = max(ans, dp(nr, nc, steps + 1) + fruits[nr][nc])
            return ans

        res = dp(n - 1, 0, 0) + dp(0, n - 1, 0)
        dp.cache_clear()
        return ans + res
        