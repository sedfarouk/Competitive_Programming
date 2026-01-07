class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        n = len(nums)

        for i in range(n):
            if target - nums[i] in h:
                return [h[target - nums[i]], i]
            h[nums[i]] = i

