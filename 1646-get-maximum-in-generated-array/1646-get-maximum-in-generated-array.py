class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        res = [-1] * (n+1)

        def dp(i):
            if res[i]!=-1: return res[i]
            if i<2: 
                res[i] = i
                return res[i]

            x = i//2
            if i%2==0:
                res[i] = dp(x)
                return res[i]
            res[i] = dp(x) + dp(x+1)
            return res[i]

        for i in range(n,-1,-1):
            dp(i)
        return max(res)
        