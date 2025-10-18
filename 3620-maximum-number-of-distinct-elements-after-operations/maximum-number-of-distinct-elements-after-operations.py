class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums[0] -= k
        ans = 1

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]

            if diff > 0:
                nums[i] = max(nums[i - 1] + 1, nums[i] - k) 
            elif abs(diff) < k:  
                nums[i] = nums[i - 1] + 1
            else:
                nums[i] = nums[i - 1]
            
            ans += nums[i] != nums[i - 1]

        return ans
                
 
