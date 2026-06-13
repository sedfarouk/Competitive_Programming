class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        tot = n
        n = list(map(int, str(n)))

        @cache
        def dp(i, tight, mask, valid, start):
            if i == len(n):
                return int(valid)

            lim = 9 if not tight else n[i]
            ans = 0

            for d in range(lim + 1):
                new_valid = valid | (mask & (1 << d)) > 0
                new_start = start | d > 0
                new_mask = (mask | (1 << d)) if new_start else mask
        
                ans += dp(i + 1, tight and d == lim, new_mask, new_valid, new_start)
            return ans

        res = dp(0, True, 0, False, False)
        dp.cache_clear()
        return tot - res