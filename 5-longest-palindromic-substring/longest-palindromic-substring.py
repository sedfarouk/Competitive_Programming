class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def findPalindrome(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1; r += 1
            return s[l + 1 : r]

        res = ""
        for i in range(n):
            pal1, pal2 = findPalindrome(i, i), findPalindrome(i, i + 1)

            if len(pal1) > len(res):
                res = pal1
            if len(pal2) > len(res):
                res = pal2

        return res