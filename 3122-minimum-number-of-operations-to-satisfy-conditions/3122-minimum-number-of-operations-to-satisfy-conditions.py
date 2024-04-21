class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        cols = list(map(list, zip(*grid)))
        
        @lru_cache(None)
        def dp(idx, prev):
            if idx==m:
                return 0

            minn = float("inf")
            for i in range(10):
                if i==prev:
                    continue
                cnt = cols[idx].count(i)
                minn = min(dp(idx+1, i) + n-cnt, minn)
            return minn
        return dp(0, -1)
            