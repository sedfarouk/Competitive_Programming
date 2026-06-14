class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        def count(x):
            n = len(x)

            @cache
            def dp(i, tight, curr):
                if i == n:
                    return int(curr == 0)

                lim = 9 if not tight else x[i]
                ans = 0

                for d in range(lim + 1):
                    ans += dp(i + 1, tight and d == lim, curr + (d if i % 2 else -d))
                return ans

            return dp(0, True, 0)

        return count(list(map(int, str(high)))) - count(list(map(int, str(low - 1))))
