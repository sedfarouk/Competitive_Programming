class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = Counter(t)
        letters = defaultdict(int)
        c = l = 0
        minn = [float("-inf"), float("inf")]
        seen = set()

        for r in range(len(s)):
            letters[s[r]] += 1
            if s[r] in cnt and s[r] not in seen and letters[s[r]] >= cnt[s[r]]:
                seen.add(s[r])
                c += 1

            while c >= len(cnt):
                if (r-l+1) < (minn[1] - minn[0] + 1):
                    minn = [l, r]

                letters[s[l]] -= 1
                if s[l] in cnt and letters[s[l]] < cnt[s[l]]:
                    seen.remove(s[l])
                    c -= 1
                
                if letters[s[l]]==0:
                    del letters[s[l]]
                l += 1

        if minn[0]==float("-inf"):
            return ""
        return s[minn[0]:minn[1]+1]