class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7

        @cache
        def dp(i, j, rem):
            if i == m - 1 and j == n - 1:
                return int((rem + grid[m - 1][n - 1]) % k == 0)

            if i == m or j == n:
                return 0

            return (dp(i + 1, j, (rem + grid[i][j]) % k) % MOD + dp(i, j + 1, (rem + grid[i][j]) % k) % MOD) % MOD

        ans = dp(0, 0, 0)
        dp.cache_clear()
        return ans