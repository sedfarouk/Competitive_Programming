class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        nums_idx = sorted([(nums[i], i) for i in range(n)])
        min_idx = n
        max_width = 0

        for val, idx in nums_idx:
            max_width = max(max_width, idx - min_idx)
            min_idx = min(min_idx, idx)

        return max_width
