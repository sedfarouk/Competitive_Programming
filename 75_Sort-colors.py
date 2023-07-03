#Leetcode 75 - 89% runtime, 73% memory

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        cnt = [0]*(max(nums)+1)
        for i in nums:
            cnt[i]+=1
        for i in range(len(cnt)):
            for j in range(cnt[i]):
                nums.append(i)
        for i in range(n):
            nums.pop(0)
                
        
        
