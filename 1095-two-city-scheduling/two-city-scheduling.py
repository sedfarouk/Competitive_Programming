class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2

        @cache
        def dp(i, c):
            if c > n:
                return float("inf")

            if i == 2 * n:
                return 0 if c == n else float("inf")

            return min(dp(i+1, c+1) + costs[i][0], dp(i+1, c) + costs[i][1])

        res = dp(0, 0)
        dp.cache_clear()
        return res
            
        