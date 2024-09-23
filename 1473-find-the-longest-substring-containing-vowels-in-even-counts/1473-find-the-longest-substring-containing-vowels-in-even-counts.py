class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        hashmap = defaultdict(int)
        vowels = {'a':1, 'e':2, 'i':4, 'o':8, 'u':16}
        cnt = 32
        hashmap[cnt] = 0
        ans = 0

        for r in range(len(s)):
            if s[r] in vowels:
                cnt ^= vowels[s[r]]

            if cnt in hashmap:
                ans = max(ans, r-hashmap[cnt]+1)
            else:
                hashmap[cnt] = r+1
        
        return ans
        
            
                

        