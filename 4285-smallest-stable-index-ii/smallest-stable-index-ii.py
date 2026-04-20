class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffMin = [nums[-1]] * n

        for i in range(n - 2, -1, -1):
            if nums[i] < suffMin[i + 1]:
                suffMin[i] = nums[i]
            else:
                suffMin[i] = suffMin[i + 1]

        prefMax = 0
        for i in range(n):
            prefMax = max(prefMax, nums[i])
            if prefMax - suffMin[i] <= k:
                return i
        return -1