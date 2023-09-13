class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        best = len(nums)
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] >= target:
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        return best
 