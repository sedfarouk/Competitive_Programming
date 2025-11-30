class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sc, tc = Counter(s), Counter(t)
        ans = 0

        for ch in ascii_letters:
            ans += abs(tc[ch] - sc[ch])

        return ans // 2