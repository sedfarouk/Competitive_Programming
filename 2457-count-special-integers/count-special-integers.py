class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        n = list(map(int, str(n)))

        @cache
        def dp(i, tight, mask):
            if i == len(n): return 1

            lim = 9 if not tight else n[i]
            ans = 0

            for d in range(lim + 1):
                if mask & (1 << d): continue
                ans += dp(i + 1, tight and d == lim, (mask | (1 << d)) if (mask or d > 0) else mask)

            return ans

        res = dp(0, True, 0)
        dp.cache_clear()
        return res - 1