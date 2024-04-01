class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dirs = [(-2,1), (-2,-1), (2,-1), (2,1), (1,2), (-1,2), (1,-2), (-1,-2)]

        @lru_cache(None)
        def dp(r, c, k):
            if k==0:
                return 0<=r<n and 0<=c<n
            if r<0 or r>=n or c<0 or c>=n:
                return 0

            ans = 0
            for x, y in dirs:
                ans += dp(r+x, c+y, k-1)
            return ans/8
        
        return dp(row, column, k)

