class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]*(amount+1)

        for i in range(1, amount+1):
            mini = float("inf")

            for coin in coins:
                if i-coin >= 0:
                    mini = min(mini, dp[i-coin]+1)
            dp[i] = mini
        return dp[amount] if dp[amount]!=float("inf") else -1
            
    
#         memo = {}

#         def dp(i):
#             if i in memo: return memo[i]
#             if i==0: return 0
#             if i < 0: return float("inf")

#             memo[i] = min(dp(i-coin)+1 for coin in coins)
#             return memo[i]
#         ans = dp(amount)
#         return ans if ans!=float("inf") else -1