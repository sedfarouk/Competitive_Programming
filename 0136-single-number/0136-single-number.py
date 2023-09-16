class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = Counter(nums)

        for key, val in nums.items():
            if val==1:
                return key

        