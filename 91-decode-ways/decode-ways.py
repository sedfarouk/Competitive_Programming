class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if s[0] == '0':
            return 0

        one_back = two_back = 1

        for i in range(1, n):
            current = 0

            if s[i] != '0':
                current = one_back
            
            two_digit = int(s[i-1:i+1])
            if 26 >= two_digit >= 10:
                current += two_back
            two_back = one_back
            one_back = current

        return one_back

        # @lru_cache
        # def dp(i):
        #     if i == n:
        #         return 1

        #     ans = 0
        #     if s[i] != '0':
        #         ans = dp(i + 1)
        #         if i < n - 1 and int(s[i:i+2]) < 27:
        #             ans += dp(i + 2)

        #     return ans

        # return dp(0)
                