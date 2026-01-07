class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = defaultdict(int)
        n = len(s)
        res = l = 0

        for r in range(n):
            h[s[r]] += 1

            while h[s[r]] > 1:
                h[s[l]] -= 1

                if h[s[l]] == 0:
                    del h[s[l]]
                
                l += 1

            res = max(res, r - l + 1)
        
        return res