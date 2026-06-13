class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        n = list(map(int, str(n)))

        @cache
        def dp(i, tight, mask):
            if i == len(n): return 1

            lim = 9 if not tight else n[i]
            return sum(dp(i+1, tight and d==lim, (mask | (1<<d)) if (mask or d>0) else mask) for d in range(lim+1) if not mask & (1<<d))

        res = dp(0, True, 0)
        dp.cache_clear()
        return res - 1