class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1):
            for j in range(i,len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j] = nums[j], nums[i]
                
        
        