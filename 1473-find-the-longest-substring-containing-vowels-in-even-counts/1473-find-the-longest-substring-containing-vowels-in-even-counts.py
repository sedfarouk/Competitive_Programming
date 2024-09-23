class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        hashmap = defaultdict(int)
        cnt = (2**5)-1
        hashmap[cnt] = 0
        ans = 0

        for r in range(len(s)):
            if s[r]=='a':
                cnt ^= 1
            elif s[r]=='e':
                cnt ^= 2
            elif s[r]=='i':
                cnt ^= 4
            elif s[r]=='o':
                cnt ^= 8
            elif s[r]=='u':
                cnt ^= 16

            if cnt in hashmap:
                ans = max(ans, r-hashmap[cnt]+1)
            else:
                hashmap[cnt] = r+1
        
        return ans
        
            
                

        