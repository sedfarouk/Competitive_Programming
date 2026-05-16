class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while r and nums[0] == nums[r]:
            r -= 1

        first, last = nums[l], nums[r]
        ans = float("inf")
        while l <= r:
            m = l + (r - l) // 2
            ans = min(ans, nums[m])

            if first <= nums[m] > last:
                l = m + 1 
            else:
                r = m - 1

        return ans
