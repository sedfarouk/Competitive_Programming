class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        ans = 0
        n = len(nums)

        @cache
        def dp(j, i):
            if i == n:
                return 0

            ans = dp(-1, i + 1)

            if colors[i] != j:
                return max(ans, dp(colors[i], i + 1) + nums[i])
            return ans

        return dp(-1, 0)