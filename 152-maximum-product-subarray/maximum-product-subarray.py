class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = max_so_far = min_so_far = nums[0]

        for i in range(1, n):
            curr = nums[i]

            temp_max = max(max_so_far * curr, min_so_far * curr, curr)
            min_so_far = min(min_so_far * curr, max_so_far * curr, curr)
            max_so_far = temp_max

            res = max(res, max_so_far)

        return res

        # @cache
        # def dp(i, p):
        #     if i == n:
        #         return p

        #     return max(dp(i + 1, p * nums[i]), dp(i + 1, nums[i]), p)

        # res = dp(1, nums[0])
        # return res