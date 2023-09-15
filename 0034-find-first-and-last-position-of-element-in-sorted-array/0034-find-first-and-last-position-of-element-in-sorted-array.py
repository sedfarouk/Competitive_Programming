class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = -1, len(nums)
        first = -1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        
        first = right
        
        left, right = -1, len(nums)

        while left + 1 < right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                left = mid
            else:
                right = mid

        second = left

        if (first or second) == -1 or second < first:
            return [-1, -1]
        return [first, second]
            