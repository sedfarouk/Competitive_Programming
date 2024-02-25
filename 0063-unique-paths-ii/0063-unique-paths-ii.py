class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}

        def safe_state(i, j):
            return 0<=i<m and 0<=j<n and obstacleGrid[i][j] != 1

        def dp(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            if not safe_state(r, c):
                return 0
            if r==0 and c==0:
                return 1
            memo[(r, c)] = dp(r-1, c) + dp(r, c-1)
            return memo[(r, c)]

        return dp(m-1, n-1)

            

        