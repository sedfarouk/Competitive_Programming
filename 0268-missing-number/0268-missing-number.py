class Solution:
    def missingNumber(self, nums: List[int]) -> int: 
        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]
            
        for i in range(len(nums)+1):
            ans ^= i
        return ans



                