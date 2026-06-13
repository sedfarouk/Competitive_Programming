class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count(x):
            n = len(x)

            @cache
            def dp(i, tight, mod, cnt, start):
                if i == n:
                    y = n - start
                    return int(mod == 0 and start >= 0 and cnt == y // 2)

                lim = 9 if not tight else int(x[i])
                ans = 0

                for d in range(lim + 1): 
                    if start == -1 and d > 0 and (n - i) % 2:
                        continue
                    if start == -1 and d == 0:
                        ans += dp(i + 1, False, 0, 0, -1)
                    else:
                        ans += dp(i + 1, tight and d == lim, (mod * 10 + d) % k, cnt + (d % 2), start if start >= 0 else i)

                return ans
            return dp(0, True, 0, 0, -1)

        return count(str(high)) - count(str(low - 1))