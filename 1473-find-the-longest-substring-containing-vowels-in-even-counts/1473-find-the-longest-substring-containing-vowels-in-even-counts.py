class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        hashmap = defaultdict(int)
        cnt = (0, 0, 0, 0, 0)
        hashmap[cnt] = 0
        ans = 0

        for r in range(len(s)):
            cnt = (cnt[0]+(s[r]=='a'), cnt[1]+(s[r]=='e'), cnt[2]+(s[r]=='i'), cnt[3]+(s[r]=='o'), cnt[4]+(s[r]=='u'))
            exp = (cnt[0]%2, cnt[1]%2, cnt[2]%2, cnt[3]%2, cnt[4]%2) 

            if exp in hashmap:
                ans = max(ans, r-hashmap[exp]+1)
            else:
                hashmap[exp] = r+1
        
        return ans
        
            
                

        