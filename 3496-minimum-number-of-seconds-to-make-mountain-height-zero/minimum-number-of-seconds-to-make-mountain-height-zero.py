class Solution:
    def minNumberOfSeconds(self, mH: int, wT: List[int]) -> int:
        n = len(wT)
        wT.sort()

        def bs(lim, w):
            l = rem = 0
            r = lim
            while l <= r:
                m = l + (r - l) // 2

                if w * (m * (m + 1) // 2) <= lim:
                    rem = m
                    l = m + 1
                else:
                    r = m - 1
            return rem 

        def f(ux):
            h = mH

            for i in range(n):
                rem = bs(ux, wT[i])
                h -= rem

                if h <= 0:
                    return True
            return False

        l, r = 1, (mH * (mH + 1) // 2) * max(wT)
        ans = r

        while l <= r:
            m = (l + r) // 2

            if f(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans