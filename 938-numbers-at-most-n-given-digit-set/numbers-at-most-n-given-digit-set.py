class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits = [int(x) for x in digits]

        n = str(n)
        l1, l2 = len(n), len(digits)

        @cache
        def dp(i, tight, g):
            if i == l1:
                return 0

            lim = 9 if not tight else int(n[i])

            ans = 0
            for j in range(l2):
                new_g = g or digits[j] > lim

                if new_g and i == l1 - 1:
                    continue
                ans += dp(i + 1, tight and digits[j] == lim, new_g) + 1

            return ans

        return dp(0, True, False)