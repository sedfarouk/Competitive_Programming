class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = [] 
        for i in range(0, len(nums), 2): 
            freq = nums[i]
            val = nums[i+1]  
            ans += [val] * freq
        return ans