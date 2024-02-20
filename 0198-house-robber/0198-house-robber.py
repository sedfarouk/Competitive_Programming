class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)-1
        memo = {}
        
        def dp(idx):
            if idx in memo: return memo[idx]
            if idx>=n: return max(0, nums[idx])
            if idx==n-1: return max(nums[-1], nums[-2])
            
            memo[idx] = max(dp(idx+1), dp(idx+2) + nums[idx])
            return memo[idx]
        
        return dp(0)
        