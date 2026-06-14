class Solution:
    def countDistinct(self, n: int) -> int:
        digits = list(map(int, str(n)))
        n = len(digits)

        @cache
        def dp(i, tight, start):
            if i == n: return 1

            lim = 9 if not tight else digits[i]
            ans = 0

            for d in range(lim + 1):
                if start and d == 0: continue
                if not start: ans += dp(i + 1, tight and d == lim, d > 0)
                else: ans += dp(i + 1, tight and d == lim, start)
            
            return ans

        res = dp(0, True, False) - 1
        dp.cache_clear()
        return res

