class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                prod = abs((nums[i]-1)*(nums[j]-1))
                ans = max(ans, prod)
        return ans