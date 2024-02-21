class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def dp(i, j):
            if i > j: return 0
            if (i, j) in memo: return memo[(i, j)]

            memo[(i, j)] = max(dp(i+1, j), nums[i] + dp(i+2, j))
            return memo[(i, j)]
        return nums[0] if len(nums)==1 else max(dp(0, len(nums)-2), dp(1, len(nums)-1))

