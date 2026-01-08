class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = float("inf")
        ans = 0

        for p in prices:
            mn = min(mn, p)
            ans = max(ans, p - mn)

        return ans