class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        l = len(s)

        @cache
        def dp(i, tight):
            if i == l:
                return 0

            lim = int(s[i]) if tight else 9
            ans = 0

            for d in range(lim + 1):
                new_tight = tight and (d == lim)
                ans += self.count_remaining(i + 1, new_tight, s) if d == 1 else 0
                ans += dp(i + 1, new_tight)
            return ans

        return dp(0, True)

    def count_remaining(self, i, tight, s):
        if i == len(s):
            return 1
        if not tight:
            return 10 ** (len(s) - i)
        return int(s[i:]) + 1