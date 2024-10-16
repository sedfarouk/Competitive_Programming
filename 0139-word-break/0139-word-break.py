class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wordDict = set(wordDict)
        n = len(s)
        # dp = [False]*(n+1)
        # dp[0] = True

        # for i in range(1, n+1):
        #     for j in range(i):
        #         if dp[j] and s[j:i] in wordDict:
        #             dp[i] = True
        #             break
        
        # return dp[n]

        @cache
        def dp(i):
            if i==n:
                return True

            for j in range(i + 1, n + 1):
                if dp(j) and s[i:j] in wordDict:
                    return True
            return False
        return dp(0)