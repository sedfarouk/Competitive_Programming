class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ''

        def palindromeLength(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1; r += 1 
            return s[l+1:r]

        for i in range(n):
            pal1 = palindromeLength(i, i)
            pal2 = palindromeLength(i, i+1)

            if len(pal1) > len(ans): ans = pal1
            if len(pal2) > len(ans): ans = pal2
        
        return ans