class Solution:
    def validPalindrome(self, s: str) -> bool:
        @cache
        def dp(l, r, used=False):
            if l > r:
                return True

            if s[l] == s[r]:
                return dp(l + 1, r - 1, used)
            if used:
                return False

            return dp(l + 1, r, True) or dp(l, r - 1, True)

        return dp(0, len(s) - 1)