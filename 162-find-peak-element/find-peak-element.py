class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(float("-inf"))
        l, r = 0, n

        while l <= r:
            m = l + (r - l) // 2

            if m > 0 and nums[m - 1] < nums[m] > nums[m + 1]:
                return m
            elif nums[m] <= nums[m + 1] and nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1

        return 0