MOD = (10 ** 9) + 7
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def count(x):
            n = len(x)

            @cache
            def dp(i, tight, curr):
                if i == n: return curr >= min_sum

                lim = 9 if not tight else int(x[i])
                ans = 0

                for d in range(lim + 1):
                    if curr + d <= max_sum:
                        ans = (ans + dp(i + 1, tight and d == lim, curr + d) % MOD) % MOD
                
                return ans

            return dp(0, True, 0) % MOD
        
        return (count(num2) - count(num1) + int(min_sum <= sum(int(x) for x in num1) <= max_sum)) % MOD