# 713. Leetcode - Subarray Product Less Than K

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        prod, left, ans = 1, 0, 0

        min_num = min(nums)
        if min_num >= k:
            return 0

        for right in range(len(nums)):
            prod*=nums[right]
            
            if prod < k:
                ans+=right-left+1

            else:
                while prod >= k and left < right:
                    prod/=nums[left]
                    left+=1
                if prod < k:
                    ans+=right-left+1

        return ans
