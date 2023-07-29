# 169. LeetCode - Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        l = len(nums)//2

        for key in nums_counter:
            if nums_counter[key] > l:
                return key
