class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                if text1[i]==text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        return dp[-1][-1]
        
#         TOP-DOWN APPROACH

#         m, n = len(text1)-1, len(text2)-1
#         memo = {}

#         def dp(i, j):
#             if (i, j) in memo:
#                 return memo[(i, j)]
            
#             if i<0 or j<0:
#                 return 0

#             if text1[i]==text2[j]:
#                 memo[(i, j)] = dp(i-1, j-1) + 1
#             else:
#                 memo[(i, j)] = max(dp(i, j-1), dp(i-1, j))
#             return memo[(i, j)]

#         return dp(m, n)