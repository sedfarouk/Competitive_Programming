class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dp(i, p):
            if i == n:
                return p

            return max(dp(i + 1, p * nums[i]), dp(i + 1, nums[i]), p)

        res = dp(1, nums[0])
        return res