class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        maxx, minn = max(nums[:3]), min(nums[:3])

        if len(nums) <= 2:
            return -1
        for i in range(3):
            if nums[i] !=maxx and nums[i] != minn:
                return nums[i]
        
