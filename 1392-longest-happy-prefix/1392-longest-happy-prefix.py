class Solution:
    def longestPrefix(self, s: str) -> str:
        # APPROACH 1 - KNUTH MORRIS PRATT (KMP) ALGORITHM
        n = len(s)
        lps = [0]*n
        i = 1
        idx = 0

        while i < n:
            if s[i]==s[idx]:
                lps[i] = idx + 1
                idx += 1
                i += 1
            else:
                if idx != 0:
                    idx = lps[idx-1]
                else:
                    lps[i] = 0
                    i += 1
        return s[:lps[-1]]
        
        # APPROACH 2 - RABIN-KARP (ROLLING HASH) ALGORITHM
        
        # MOD, n = (10**9)+7, len(s)
        # ans = ""
        # p = 1

        # prefix_hash = suffix_hash = 0
        # for i in range(n-1):
        #     prefix_hash = ((prefix_hash*29)+ord(s[i])-96)%MOD
        #     suffix_hash = (suffix_hash+(ord(s[-i-1])-96)*p)%MOD
        #     p = (p*29)%MOD

        #     if suffix_hash==prefix_hash:
        #         ans = s[:i+1]
        
        # return ans