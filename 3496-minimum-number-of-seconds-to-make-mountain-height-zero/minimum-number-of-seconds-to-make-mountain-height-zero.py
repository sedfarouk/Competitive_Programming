class Solution:
    def minNumberOfSeconds(self, mH: int, wT: List[int]) -> int:
        def f(T):
            h = mH

            for w in wT:
                k = int((math.sqrt(1 + 8*T//w) - 1) // 2) # Simplified through quadratic formula
                h -= k

                if h <= 0:
                    return True

            return False

        l, r = 1, max(wT) * (mH * (mH + 1) // 2)
        ans = r

        while l <= r:
            m = (l + r) // 2

            if f(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans