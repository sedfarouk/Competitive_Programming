# 2592. Leetcode - Maximize Greatness Of An Array

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        temp = []
        ans = 0
        dup = float("inf")

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1] or nums[i]==nums[i-1] and nums[i]==dup:
                temp.append(nums[i])
                dup = nums[i]

        ptr1, ptr2 = 0, 0                
        while ptr1 < len(temp):
            if temp[ptr1] > nums[ptr2]:
                ans+=1
                ptr2+=1
            ptr1+=1
        
        return ans
            
            
