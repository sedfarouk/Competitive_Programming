class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        
        n = len(nums)
        prev2, prev1, curr = 0, 0, 0
        prev1, prev2 = nums[-1], max(nums[-1], nums[-2])
        
        for i in range(n-3, -1, -1):
            curr = max(nums[i]+prev1, prev2)
            prev1 = prev2
            prev2 = curr           
            
        return prev2
        
#         memo = {}
        
#         def dp(idx):
#             if idx in memo: return memo[idx]
#             if idx>=n: return max(0, nums[idx])
#             if idx==n-1: return max(nums[-1], nums[-2])
            
#             memo[idx] = max(dp(idx+1), dp(idx+2) + nums[idx])
#             return memo[idx]
        
#         return dp(0)
        