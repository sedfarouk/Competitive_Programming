class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        n = len(nums)-1

        def dp(i, tot):
            if (i, tot) in memo: return memo[(i, tot)]
            if i==-1: return tot==target
            
            memo[(i, tot)] = dp(i-1, tot+nums[i-1]) + dp(i-1, tot-nums[i-1])
            return memo[(i, tot)]
        return dp(n, 0)
            