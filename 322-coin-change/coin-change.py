class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(amt):
            if amt == 0:
                return 0

            ans = float("inf")
            for c in coins:
                if amt - c >= 0:
                    ans = min(ans, dp(amt - c) + 1)

            return ans

        res = dp(amount)
        dp.cache_clear()
        return res if res != float("inf") else -1
            