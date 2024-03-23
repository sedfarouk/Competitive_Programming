class Solution:
    def longestPrefix(self, s: str) -> str:
        MOD, n = (10**9)+7, len(s)
        hashes = [0]*n
        ans = ""

        prefix_hash = 0
        for i in range(n-1):
            prefix_hash *= 29
            prefix_hash += (ord(s[i])-96) 
            prefix_hash %= MOD
            hashes[i] = prefix_hash

        s = s[::-1]
        suffix_hash = 0
        for i in range(n):
            suffix_hash += (ord(s[i])-96)*pow(29, i, MOD)
            suffix_hash %= MOD
            suffix = s[:i+1]
            
            if suffix_hash==hashes[i] and len(suffix) > len(ans):
                ans = suffix
        
        return ans[::-1]