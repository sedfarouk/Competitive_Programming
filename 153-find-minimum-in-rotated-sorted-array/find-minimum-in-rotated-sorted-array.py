class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return nums[bisect_left(nums, True, key = lambda n: n <= nums[-1])]

        l, r = 0, len(nums) - 1
        first, last = nums[l], nums[r]
        while l < r:
            m = l + (r - l) // 2

            if first <= nums[m] > last:
                l = m + 1
            else:
                r = m

        return nums[l]