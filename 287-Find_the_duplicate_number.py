# 287. Find the duplicate number - Leetcode

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp = [0] * (max(nums)+1)

        for i in nums:
            if temp[i]==0:
                temp[i]+=1
            else:
                return i
