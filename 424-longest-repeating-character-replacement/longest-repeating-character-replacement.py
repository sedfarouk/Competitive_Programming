class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = defaultdict(int)
        ans = l = 0
        n = len(s)

        for r in range(n):
            h[s[r]] += 1

            while (r - l + 1) - max(h.values()) > k:
                h[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)                     

        return ans



