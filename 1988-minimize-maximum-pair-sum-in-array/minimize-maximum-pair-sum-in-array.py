class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums) // 2
        nums.sort()
        ans = 0

        for i in range(n):
            ans = max(ans, nums[i] + nums[len(nums) - i - 1])

        return ans