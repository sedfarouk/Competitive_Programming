class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = float("-inf")

        left, right = 0, len(nums)-1
        while left < right:
            ans = max(ans, nums[left]+nums[right])
            left+=1
            right-=1
        return ans
