class Solution:
    def validPalindrome(self, s: str) -> bool:
        used = False
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                first, second = s[l+1:r+1], s[l:r]
                return first == first[::-1] or second == second[::-1]
            l += 1; r -= 1

        return True
