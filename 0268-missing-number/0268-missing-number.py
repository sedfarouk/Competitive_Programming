class Solution:
    def missingNumber(self, nums: List[int]) -> int:        
        nums.append(-1)
        ans = 0
        i = 0
        
        while i < len(nums):
            if nums[i] != i:
                if nums[i]==-1:
                    ans = i
                    i += 1
                else:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            else:
                i += 1

        return ans




                