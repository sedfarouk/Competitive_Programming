class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minn = float("inf")
        win = ""
        hashmap = defaultdict(int)
        t_cnt = Counter(t)
        cnt = left = 0

        for right in range(len(s)):
            hashmap[s[right]] += 1

            if s[right] in t_cnt and hashmap[s[right]] <= t_cnt[s[right]]:
                cnt += 1

            while cnt==len(t):
                dist = right-left+1
                if dist < minn:
                    win = s[left:right+1]
                    minn = dist

                hashmap[s[left]] -= 1
                if s[left] in t_cnt and hashmap[s[left]] < t_cnt[s[left]]:
                    cnt -= 1
                left += 1

        return win