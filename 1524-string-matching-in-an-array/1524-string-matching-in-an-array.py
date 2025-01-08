class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        n = len(words)

        for i in range(n):
            for j in range(n):
                if i != j and words[j] in words[i]:
                    ans.add(words[j])
        return list(ans)

        