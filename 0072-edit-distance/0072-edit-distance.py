class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        @lru_cache(None)
        def dp(i, j):
            if i==n:
                return m-j
            if j==m:
                return n-i
            if word1[i]==word2[j]:
                return dp(i+1, j+1)
            return 1 + min(dp(i+1, j), dp(i, j+1), dp(i+1, j+1))
        return dp(0, 0)