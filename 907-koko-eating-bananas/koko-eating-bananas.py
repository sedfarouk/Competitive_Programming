class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def f(x):
            time = 0
            for p in piles:
                time += (p + x - 1) // x
            return time <= h

        l, r = 1, max(piles)
        ans = r
        while l <= r:
            m = l + (r - l) // 2

            if f(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans

