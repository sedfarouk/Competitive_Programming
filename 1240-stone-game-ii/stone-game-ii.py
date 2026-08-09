class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suff = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suff[i] = suff[i + 1] + piles[i]
 
        @cache
        def dp(i, m):
            if i >= n: return 0

            ans = float("-inf")
            for j in range(1, 2 * m + 1):    
                if i + j > n: break            
                ans = max(ans, suff[i] - dp(i + j, max(j, m)))

            return ans
        
        res = dp(0, 1)
        dp.cache_clear()
        return res
