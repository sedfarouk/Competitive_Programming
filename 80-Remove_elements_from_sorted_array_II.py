# 80. Leetcode - Remove Elements From Sorted Array II

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 2

        while right < len(nums):
            if nums[right]==nums[left]:
                del nums[right]
                right-=1
                left-=1
            left+=1
            right+=1
            
        return len(nums)
