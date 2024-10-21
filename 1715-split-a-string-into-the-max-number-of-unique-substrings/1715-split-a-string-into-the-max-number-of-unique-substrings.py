class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        
        def backtrack(s):
            ans = 0
            for i in range(1, len(s)+1):
                if s[:i] not in seen:
                    seen.add(s[:i])
                    ans = max(ans, backtrack(s[i:]) + 1)
                    seen.remove(s[:i])
            return ans
        return backtrack(s)
        