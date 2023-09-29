class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                decreasing = False
            if nums[i] > nums[i-1]:
                increasing = False

        if increasing or decreasing:
            return True
        return False
            
        