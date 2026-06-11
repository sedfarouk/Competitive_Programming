class Solution:
    def findIntegers(self, n: int) -> int:
        bs = bin(n)[2:]
        print(bs)
        n = len(bs)

        @cache
        def dp(i, f, p):
            if i == n:
                return 1

            ans = dp(i + 1, f and (bs[i] == '0'), True)

            if (not f or int(bs[i])) and p:
                ans += dp(i + 1, f, False)

            return ans

        return dp(0, True, True)

