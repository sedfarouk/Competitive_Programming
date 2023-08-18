# 128. Leetcode - Longest Consecutive Sequence 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        ans, tmp = 1, 1
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]-nums[i-1]==1:
                tmp+=1
            else:
                ans = max(ans, tmp)
                tmp = 1
        ans = max(ans, tmp)
        return ans
