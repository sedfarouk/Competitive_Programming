# 26 - Remove Duplicates From Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seeker = holder = 0

        while seeker < len(nums):
            if nums[seeker] > nums[holder]:
                nums[holder+1], nums[seeker] = nums[seeker], nums[holder+1]
                holder+=1
            seeker += 1
        return holder+1
