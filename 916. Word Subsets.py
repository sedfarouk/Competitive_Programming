class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        cntB = Counter()

        for word in words2:
            cnt = Counter(word)

            for key, val in cnt.items():
                cntB[key] = max(cntB[key], val)

        ans = []
        for word in words1:
            cnt = Counter(word)

            if all(cnt[key] >= val for key, val in cntB.items()):
                ans.append(word)

        return ans
