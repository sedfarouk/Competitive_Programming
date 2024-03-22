class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        MOD = (10**9)+7
        n, m = len(haystack), len(needle)
        
        def get_ascii(letter):
            return ord(letter)-ord('a')+1
        
        def string_hash(s, l):
            hash_val = 0
            for i in range(l+1):
                hash_val += ((29**(l-i))*get_ascii(s[i]))
            return hash_val % MOD

        if n < m:
            return -1
        
        haystack_hash = string_hash(haystack, m-1)
        needle_hash = string_hash(needle, m-1)
        
        if haystack_hash == needle_hash:
            return 0

        for i in range(m, n):
            haystack_hash -=  get_ascii(haystack[i-m])*(29**(m-1))
            haystack_hash *= 29
            haystack_hash += get_ascii(haystack[i])
            haystack_hash %= MOD
            
            if haystack_hash == needle_hash:
                return i-m+1
        return -1
            
        
        
        
        
        