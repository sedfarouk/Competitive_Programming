# 1877. Leetcode - Minimize maximum pair sum in array

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = float("-inf")

        left, right = 0, len(nums)-1
        while left < right:
            curr = nums[left]+nums[right]
            ans = max(ans, curr)
            left+=1
            right-=1
        return ans
