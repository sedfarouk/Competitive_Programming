class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = list(set(nums))
        for i in unique:
            if nums.count(i)==1:
                return i