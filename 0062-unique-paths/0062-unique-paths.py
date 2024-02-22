class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[-1][-1] = 1
        
        def inbound_ans(i, j):
            if 0<=i<n and 0<=j<m:
                return dp[i][j]
            return 0
        
        for r in range(n-1, -1, -1):
            for c in range(m-1, -1, -1):
                dp[r][c] += inbound_ans(r+1, c) + inbound_ans(r, c+1)
        return dp[0][0]
                
        
#         memo = {}

#         def recurse(row, col):
#             if (row, col) in memo: return memo[(row, col)]
            
#             if row==0 and col==0:
#                 return 1
            
#             if row < 0 or col < 0:
#                 return 0

#             memo[(row, col)] = recurse(row, col-1) + recurse(row-1, col)
#             return memo[(row, col)]
#         return recurse(m-1, n-1)

        
        