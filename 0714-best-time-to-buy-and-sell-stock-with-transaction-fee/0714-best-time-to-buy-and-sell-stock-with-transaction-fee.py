class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n+1)]
        dp[0][0], dp[0][1] = 0, -prices[0]-fee

        for i in range(1, n+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i-1])
            dp[i][1] = max(dp[i-1][0]-prices[i-1]-fee, dp[i-1][1])
        return max(dp[n][0], dp[n][1])
