class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[0] >= nums[m] <= nums[-1] and (m == 0 or nums[m] <= nums[m - 1]):
                return nums[m]
            elif nums[m] > nums[-1]:
                l = m + 1
            else:
                r = m - 1

        

