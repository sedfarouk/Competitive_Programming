# 287. Find the duplicate number - Leetcode

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # temp = [0] * (max(nums)+1)

        # for i in nums:
        #     if temp[i]==0:
        #         temp[i]+=1
        #     else:
        #         return i

        i = 0
        n = len(nums)
        
        while i < n:
            correctIdx = nums[i]
            if nums[i] != nums[correctIdx-1]:
                nums[i], nums[correctIdx-1] = nums[correctIdx-1], nums[i]
                
            else:
                i += 1
                
        for j in range(n):
            if j != nums[j]-1:
                return nums[j]

