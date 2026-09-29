class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1)]

        if grid[0][0] == ')': return False
        
        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m

        @cache
        def dp(r, c, b):
            if r == n - 1 and c == m - 1:
                return not b

            for dr, dc in dirs:
                nr, nc = dr + r, dc + c

                if inbound(nr, nc) and grid[nr][nc] != '*':
                    x = grid[nr][nc]
                    if x == ')' and not b: return False
                    if dp(nr, nc, b + (1 if x == '(' else -1)): return True
            
            return False

        ans = dp(0, 0, (1 if grid[0][0] == '(' else -1))
        dp.cache_clear()
        return ans