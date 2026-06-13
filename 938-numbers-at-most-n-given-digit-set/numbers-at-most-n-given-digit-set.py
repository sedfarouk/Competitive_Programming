class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits = list(map(int, digits))
        n = list(map(int, str(n)))
        l1, l2 = len(n), len(digits)

        @cache
        def dp(i, tight):
            if i == l1: return 0

            lim = 9 if not tight else int(n[i])
            ans = 0

            for d in digits:
                if d > lim: ans += sum(l2 ** j for j in range(l1 - i - 1))
                else: ans += dp(i + 1, tight and d == lim) + 1

            return ans

        return dp(0, True)