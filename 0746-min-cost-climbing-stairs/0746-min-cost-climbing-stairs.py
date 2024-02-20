class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        memo = {}
        
        def dp(idx):
            if idx < 2:
                return cost[idx]
            
            if idx not in memo:
                memo[idx] =  cost[idx] + min(dp(idx-1), dp(idx-2))
            return memo[idx]
        
        return dp(len(cost)-1)
        
                
        
        
        
            