class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)

        @cache
        def dp(i, j):
            if i == n or j == m:
                return float("-inf")

            x = max(dp(i + 1, j), dp(i, j + 1))
            return max(x, dp(i + 1, j + 1) + nums1[i] * nums2[j], nums1[i] * nums2[j])

        return dp(0, 0)

