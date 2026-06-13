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

                for d in range(lim + 1):
                    if n - i <= m and int(s[m - (n - i)]) != d: continue
                    ans += dp(i + 1, tight and d == int(x[i]))
                
                return ans

            return dp(0, True)

        return count(str(finish)) - count(str(start - 1))

