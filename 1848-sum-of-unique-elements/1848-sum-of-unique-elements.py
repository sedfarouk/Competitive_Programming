class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans =0
        for i in range(len(nums)):
            if nums.count(nums[i])==1:
                ans+=nums[i]
        return ans