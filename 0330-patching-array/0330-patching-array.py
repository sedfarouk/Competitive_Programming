class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = i = 0
        cnt = 1
        
        while cnt <= n:
            if i < len(nums) and cnt >= nums[i]:
                cnt += nums[i]
                i += 1
            else:
                ans += 1
                cnt <<= 1
        return ans
            