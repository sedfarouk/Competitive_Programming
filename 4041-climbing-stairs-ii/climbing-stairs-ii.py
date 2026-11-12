class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        costs.extend([float("inf")] * 3)

        @cache
        def dp(i):
            if i >= n - 1: return 0

            return min(dp(i+1) + costs[i+1] + 1, dp(i+2) + costs[i+2] + 4, dp(i+3) + costs[i+3] + 9)
        
        return dp(-1)