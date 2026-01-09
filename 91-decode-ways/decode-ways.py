class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @lru_cache
        def dp(i):
            if i == n:
                return 1

            ans = 0
            if s[i] != '0':
                ans = dp(i + 1)
                if i < n - 1 and int(s[i:i+2]) < 27:
                    ans += dp(i + 2)

            return ans

        return dp(0)
                