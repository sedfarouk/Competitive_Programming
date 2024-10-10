class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        rightMax = [None]*n
        rightMax[-1] = nums[-1]

        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], nums[i])

        left = right = max_width = 0
        while right < n:
            while left < right and nums[left] > rightMax[right]:
                left += 1
            max_width = max(max_width, right-left)
            right += 1
        
        return max_width

        # n = len(nums)
        # nums_idx = sorted([(nums[i], i) for i in range(n)])
        # min_idx = n
        # max_width = 0

        # for val, idx in nums_idx:
        #     max_width = max(max_width, idx - min_idx)
        #     min_idx = min(min_idx, idx)

        # return max_width
