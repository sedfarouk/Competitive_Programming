class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        us = sorted([sorted(x) for x in units], key=lambda x:(x[1] if len(x) > 1 else x[0]), reverse=True)
        ans = 0

        for u in us[:-1]:
            if len(u) > 1:
                ans += u[1]
                us[-1].append(u[0])
            else:
                ans += u[0]
        
        ans += min(us[-1])
        return ans



