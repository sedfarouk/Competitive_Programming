MOD = 10**9 + 7
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        @cache
        def dp(r, c, d):
            if r < 0 or r == n or c < 0 or c == m: return 0
            if r == c == 0: return 1

            if grid[r][c] == 1: 
                if d == 1: return dp(r, c - 1, -1)
                return dp(r - 1, c, 1)

            return (dp(r - 1, c, 1) % MOD + dp(r, c - 1, -1) % MOD) % MOD
            
        res = dp(n - 1, m - 1, 0)
        dp.cache_clear()
        return res

