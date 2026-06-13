class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits = list(map(int, digits))
        n = list(map(int, str(n)))

        @cache
        def dp(i, tight, g):
            if i == len(n): return 0

            lim = 9 if not tight else int(n[i])
            ans = 0
            
            for d in digits:
                new_g = g or d > lim
                if new_g and i == len(n) - 1: continue
                ans += dp(i + 1, tight and d == lim, new_g) + 1

            return ans

        return dp(0, True, False)