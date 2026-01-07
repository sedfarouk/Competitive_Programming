class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = curr = 0
        for num in nums:
            if num:
                curr += 1
            else:
                res = max(res, curr)
                curr = 0

        res = max(res, curr)
        return res
