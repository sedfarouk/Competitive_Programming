class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        us = sorted([sorted(x, reverse=True) for x in units], key=lambda x:(x[-2] if len(x) > 1 else x[-1]), reverse=True)
        print(us)
        ans = 0

        for u in us:
            if len(u) > 1:
                ans += u[-2]
                if u[-1] < us[-1][-1]: us[-1].append(u[-1])
            else:
                ans += u[-1]

        if len(us[-1]) > 1:
            ans = ans - us[-1][-2] + us[-1][-1]
        return ans 



