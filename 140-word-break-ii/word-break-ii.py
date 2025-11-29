class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordDict = set(wordDict)
        curr = []

        def backtrack(idx):
            if idx == n:
                ans.append(" ".join(curr))
                return 

            for i in range(idx, n):
                if s[idx : i + 1] in wordDict:
                    curr.append(s[idx : i + 1])
                    backtrack(i + 1)
                    curr.pop()

        ans = []
        backtrack(0)
        return ans