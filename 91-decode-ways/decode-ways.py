class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @cache
        def dp(i):
            if i == n:
                return 1

            if s[i] == '0':
                return 0

            x = dp(i + 1) 
            y = dp(i + 2) if 9 < int(s[i:i+2]) < 27 else 0
            return x + y

        ans = dp(0)
        dp.cache_clear()
        return ans