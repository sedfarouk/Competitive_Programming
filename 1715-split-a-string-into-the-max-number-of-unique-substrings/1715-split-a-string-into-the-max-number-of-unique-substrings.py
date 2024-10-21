class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        res = [0]
        
        def backtrack(idx):
            if idx==len(s):
                res[-1] = max(res[-1], len(seen))
                return

            for i in range(idx + 1, len(s) + 1):
                if s[idx : i] not in seen:
                    seen.add(s[idx : i])
                    backtrack(i)
                    seen.remove(s[idx : i])
        backtrack(0)
        return res[-1]
        