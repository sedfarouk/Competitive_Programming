class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1, 0, -1) :
            if nums[i] < nums[i-1] + nums[i-2] and i-2>=0:
                return nums[i] + nums[i-1] + nums[i-2]
        return 0

