class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==1 and nums[0]==target:
            return [0,0]

        left, right = 0, len(nums)-1
        leftmost, rightmost = -1, -1

        while left <= right:
            mid = left + (right-left) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                leftmost = mid
                right = mid - 1
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2

            if nums[mid] > target:
                right = mid - 1
            else:
                rightmost = mid
                left = mid + 1
        
        if leftmost==-1 or rightmost==-1 or leftmost > rightmost:
            return [-1, -1]
        return [leftmost, rightmost]
            