class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        m = len(s)

        def count(x):
            n = len(x)

            if n < m: return 0

            @cache
            def dp(i, tight):
                if i == n: return 1

                lim = min(limit, limit if not tight else int(x[i]))
                ans = 0

                if n - i <= m:
                    curr = int(s[m - (n - i)])
                    if lim < curr: return 0
                    else: ans += dp(i + 1, tight and curr == lim)
                else:
                    for d in range(lim + 1):
                        ans += dp(i + 1, tight and d == int(x[i]))
                
                return ans

            return dp(0, True)

        return count(str(finish)) - count(str(start - 1))

