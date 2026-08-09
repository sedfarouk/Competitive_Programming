class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        @cache
        def dp(i, t, m):
            if i >= n: return 0

            ans = float("-inf") if t else float("inf")
            summ = 0
            for j in range(i, min(n, i + 2 * m)):
                summ += piles[j]
                
                if t: ans = max(ans, dp(j + 1, not t, max(j - i + 1, m)) + summ)
                else: ans = min(ans, dp(j + 1, not t, max(j - i + 1, m)))

            return ans
        
        res = dp(0, True, 1)
        dp.cache_clear()
        return res
