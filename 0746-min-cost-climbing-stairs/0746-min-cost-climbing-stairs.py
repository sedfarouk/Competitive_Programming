class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost.append(0)
        
        dp = [0]*(n+1)
        dp[0], dp[1] = cost[0], cost[1]
        
        for i in range(2, n+1):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return dp[n]
    
#         memo = {}
        
#         def dp(i):
#             if i in memo: return memo[i]
#             if i<2: return cost[i]
            
#             memo[i] = cost[i] + min(dp(i-1), dp(i-2))
#             return memo[i]
#         return dp(n)