class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = float("inf")
        ans = 0

        for num in prices:
            ans = max(ans, num - mn)
            mn = min(mn, num)

        return ans
