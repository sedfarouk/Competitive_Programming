MOD = 10**9 + 7

class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        def valid(num):
            for i in range(1, len(num)):
                if abs(int(num[i]) - int(num[i - 1])) != 1:
                    return 0
            return 1

        def count(x):
            n = len(x)

            @cache
            def dp(i, tight, prev, start):
                if i == n: return int(start)

                lim = 9 if not tight else int(x[i])
                ans = 0

                for d in range(lim + 1):
                    if d == 0 and not start: 
                        ans = (ans + dp(i + 1, False, 0, False)) % MOD
                    elif abs(prev - d) == 1 or (not start and d > 0): 
                        ans = (ans + dp(i + 1, tight and d == lim, d, start or d > 0)) % MOD

                return ans

            return dp(0, True, 0, False)

        return (count(high) - count(low) + valid(low)) % MOD
            