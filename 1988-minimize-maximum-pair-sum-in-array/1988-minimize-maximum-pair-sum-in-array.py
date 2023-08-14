class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = float("-inf")

        for i in range(len(nums)//2):
            ans = max(ans, nums[i]+nums[len(nums)-1-i])
        return ans
