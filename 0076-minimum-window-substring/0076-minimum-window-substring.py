class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""

        hashmap = defaultdict(int)
        t_count = Counter(t)
        left = 0
        ans = ""
        min_win = float("inf")
        cnt = 0

        for right in range(len(s)):
            hashmap[s[right]] += 1

            if s[right] in t and hashmap[s[right]] <= t_count[s[right]]:
                cnt+=1
            
            while cnt==len(t):
                if right-left+1 < min_win:
                    min_win = right-left+1
                    ans = s[left:right+1]
                hashmap[s[left]] -= 1
                if s[left] in t and hashmap[s[left]] < t_count[s[left]]:
                    cnt-=1
                left+=1
        return ans 
        