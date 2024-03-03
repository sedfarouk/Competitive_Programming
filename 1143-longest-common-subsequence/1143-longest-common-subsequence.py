class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1)-1, len(text2)-1
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i<0 or j<0:
                return 0

            if text1[i]==text2[j]:
                memo[(i, j)] = dp(i-1, j-1) + 1
            else:
                memo[(i, j)] = max(dp(i, j-1), dp(i-1, j))
            return memo[(i, j)]

        return dp(m, n)