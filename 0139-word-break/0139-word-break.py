class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        return dp[n]

        # @cache
        # def dp(i, curr):
        #     if i==n:
        #         return curr in wordDict

        #     ans = dp(i+1, curr + s[i])
        #     if curr in wordDict:
        #         ans |= dp(i+1, s[i]) 
        #     return ans
        # res = dp(0, "")
        # dp.cache_clear()
        # return res