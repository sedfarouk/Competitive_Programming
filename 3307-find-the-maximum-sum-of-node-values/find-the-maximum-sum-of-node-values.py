class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[n][0] = float("-inf")

        for i in range(n - 1, -1, -1):
            for j in [0, 1]:
                dp[i][j] = max(dp[i + 1][j] + nums[i], dp[i + 1][j ^ 1] + (nums[i] ^ k))

        return dp[0][1]


        # @cache
        # def dp(i, isEven):
        #     if i == n:
        #         return 0 if isEven else float("-inf")

        #     return max(dp(i + 1, isEven) + nums[i], dp(i + 1, isEven ^ 1) + (nums[i] ^ k))

        # ans = dp(0, True)
        # dp.cache_clear()
        # return ans