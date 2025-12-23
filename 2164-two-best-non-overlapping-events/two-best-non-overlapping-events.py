class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        starts = [s for s, _, _ in events]
        suff = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suff[i] = max(suff[i + 1], events[i][2])

        ans = 0
        for _, end, val in events:
            ans = max(ans, val + suff[bisect_right(starts, end)])

        return ans        
        
        # @cache
        # def dp(i, p):
        #     if i == n:
        #         return 0

        #     _, end, val = events[i]
            
        #     if p:
        #         return max(val, dp(i + 1, True))
        #     return max(dp(bisect_right(events, [end, float("inf")]), True) + val, dp(i + 1, False))

        # res = dp(0, False)
        # dp.cache_clear()
        # return res