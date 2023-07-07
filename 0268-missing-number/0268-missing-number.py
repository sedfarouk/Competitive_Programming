class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (set(range(len(nums)+1))-(set(nums))).pop()
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
