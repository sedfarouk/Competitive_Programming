class Solution:
    def __init__(self, memo={}):
        self.memo = memo

    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        
        if n-2 < 0 or n-1 < 0:
            return 1

        self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n]

        
        