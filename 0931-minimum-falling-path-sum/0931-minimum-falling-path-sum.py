class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # BOTTOM-UP
        m, n = len(matrix), len(matrix[0])

        for r in range(m-2, -1, -1):
            for c in range(n-1, -1, -1):
                bottom = matrix[r+1][c]
                left_bottom = float("inf") if c-1<0 else matrix[r+1][c-1]
                right_bottom = float("inf") if c+1==n else matrix[r+1][c+1]
                matrix[r][c] += min(bottom, left_bottom, right_bottom)
        
        return min(matrix[0])


        # TOP DOWN
        # memo = {}

        # def inbound(i, j):
        #     return 0<=i<m and 0<=j<n

        # def dp(r, c):
        #     if (r, c) in memo:
        #         return memo[(r, c)]

        #     if not inbound(r, c):
        #         return float("inf")

        #     if r==m-1:
        #         return matrix[r][c]
        #     memo[(r, c)] = matrix[r][c] + min(dp(r+1, c), dp(r+1, c-1), dp(r+1, c+1))
        #     return memo[(r, c)]

        # minn = float("inf")
        # for i in range(len(matrix[0])):
        #     minn = min(dp(0, i), minn)
        # return minn
        
