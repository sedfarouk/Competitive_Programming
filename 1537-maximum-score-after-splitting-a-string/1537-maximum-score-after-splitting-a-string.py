class Solution:
    def maxScore(self, s: str) -> int:
        curr = s.count('1')
        ans = zeros = 0

        for ch in s[:-1]:
            curr -= int(ch)
            zeros += int(ch) ^ 1
            ans = max(ans, curr + zeros)
        return ans