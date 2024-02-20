class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost.append(0)
        memo = {}
        
        def dp(idx):
            if idx in memo: return memo[idx]
            
            if idx < 2:
                return cost[idx]
 
            memo[idx] =  cost[idx] + min(dp(idx-1), dp(idx-2))
            return memo[idx]
        
        return dp(n)
        
                
        
        
        
            