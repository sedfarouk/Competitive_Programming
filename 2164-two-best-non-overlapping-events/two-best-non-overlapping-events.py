class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()

        @cache
        def dp(i, p):
            if i == n:
                return 0

            _, end, val = events[i]
            
            if p:
                return max(val, dp(i + 1, True))
            return max(dp(bisect_right(events, [end, float("inf")]), True) + val, dp(i + 1, False))

        res = dp(0, False)
        dp.cache_clear()
        return res