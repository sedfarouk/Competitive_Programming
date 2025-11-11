class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @lru_cache(None)
        def dp(i, a, b):
            if (a == 0 and b == 0) or i == len(strs):
                return 0

            zeros = strs[i].count('0')
            ones = len(strs[i]) - zeros

            ans = dp(i + 1, a, b)
            if a >= zeros and b >= ones:
                ans = max(ans, dp(i + 1, a - zeros, b - ones) + 1)
            return ans

        res = dp(0, m, n)
        dp.cache_clear()
        return res
            
        