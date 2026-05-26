class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0': return False
        n = len(s)

        dp = [False] * n
        dp[0] = True
        maxReach, count = maxJump, 0

        for i in range(minJump, n):
            if i > maxReach:
                return False

            count += dp[i - minJump]

            if i > maxJump:
                count -= dp[i - maxJump - 1]
            
            if count > 0 and s[i] == '0':
                dp[i] = True
                maxReach = i + maxJump
        
        return count > 0