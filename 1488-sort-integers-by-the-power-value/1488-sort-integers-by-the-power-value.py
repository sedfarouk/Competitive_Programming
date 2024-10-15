class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        def dp(num):
            if num==1:
                return 0

            if num in memo:
                return memo[num]

            if num % 2:
                memo[num] = dp(num * 3 + 1) + 1
            else:
                memo[num] = dp(num // 2) + 1
            return memo[num]

        hmap = {}
        for x in range(lo, hi+1):
            hmap[x] = dp(x)

        vals = sorted([x for x in hmap.keys()], key=lambda x:(hmap[x], x))
        return vals[k-1]