class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res, words = [], []
        n = len(s)

        def backtrack(i):
            if i == n:
                res.append(" ".join(words)) 
                return

            for j in range(i, n):
                if s[i : j + 1] in wordDict:
                    words.append(s[i : j + 1])
                    backtrack(j + 1)
                    words.pop()

        backtrack(0)
        return res
