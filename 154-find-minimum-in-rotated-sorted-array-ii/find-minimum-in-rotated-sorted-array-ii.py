class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while r and nums[0] == nums[r]:
            r -= 1

        first, last = nums[l], nums[r]
        while l < r:
            m = l + (r - l) // 2

            if first <= nums[m] > last:
                l = m + 1
            else:
                r = m

        return nums[l]
