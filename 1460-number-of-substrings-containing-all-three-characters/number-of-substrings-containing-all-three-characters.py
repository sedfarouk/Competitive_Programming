class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        h = defaultdict(int)
        ans = l = 0

        for r in range(n):
            h[s[r]] += 1

            while len(h) > 2:
                h[s[l]] -= 1

                if not h[s[l]]: del h[s[l]]
                l += 1

            ans += r - l + 1

        return (n * (n + 1) // 2) - ans