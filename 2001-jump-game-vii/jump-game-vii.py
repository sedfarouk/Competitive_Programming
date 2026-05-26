class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0': return False
        n = len(s)

        dp = [False] * n
        dp[0] = True
        count = 0

        for i in range(minJump, n):
            count += dp[i - minJump]

            if i > maxJump:
                count -= dp[i - maxJump - 1]
            
            if count > 0 and s[i] == '0':
                dp[i] = True
        
        return count > 0