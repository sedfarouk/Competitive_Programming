class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vows = ['a', 'e', 'i', 'o', 'u']
        pref = [0]

        for w in words:
            pref.append(pref[-1])
            if w[0] in vows and w[-1] in vows:
                pref[-1] += 1

        res = []
        for l, r in queries:
            res.append(pref[r + 1] - pref[l])
        return res
        
