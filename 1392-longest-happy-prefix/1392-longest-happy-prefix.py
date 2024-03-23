class Solution:
    def longestPrefix(self, s: str) -> str:
        MOD, n = (10**9)+7, len(s)
        ans = ""

        prefix_hash = suffix_hash = 0
        for i in range(n-1):
            prefix_hash = ((prefix_hash*29)+ord(s[i])-96)%MOD
            suffix_hash = (suffix_hash+(ord(s[-i-1])-96)*pow(29,i,MOD))%MOD

            if suffix_hash==prefix_hash:
                ans = s[:i+1]
        
        return ans