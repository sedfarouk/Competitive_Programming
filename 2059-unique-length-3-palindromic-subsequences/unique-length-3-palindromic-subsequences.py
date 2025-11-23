class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0

        for c in 'abcdefghijklmnopqrstuvwxyz':
            first, last = s.find(c), s.rfind(c)
            if first >= 0: ans += len(set(s[first + 1:last]))

        return ans

        