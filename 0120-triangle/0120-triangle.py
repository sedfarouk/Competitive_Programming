class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0]*n for _ in range(n)]
        dp[-1] = triangle[-1]

        for r in range(n-2, -1, -1):
            for c in range(r+1):
                dp[r][c] = min(dp[r+1][c], dp[r+1][c+1]) + triangle[r][c]

        return dp[0][0]

                