class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)

        @cache
        def dp(i, isEven):
            if i == n:
                return 0 if isEven else float("-inf")

            return max(dp(i + 1, isEven) + nums[i], dp(i + 1, isEven ^ 1) + (nums[i] ^ k))

        ans = dp(0, True)
        dp.cache_clear()
        return ans