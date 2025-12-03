class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        def cntPalindrome(l, r):
            cnt = 0
            while l >= 0 and r < n and s[l] == s[r]:
                cnt += 1
                l -= 1; r += 1 
            return cnt

        for i in range(n):
            ans += cntPalindrome(i, i) + cntPalindrome(i, i+1)
        
        return ans