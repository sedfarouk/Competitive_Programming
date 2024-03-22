class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def get_ascii(ch):
            return ord(ch)-ord('a')+1
        
        s = s[::-1]
        s_hash, n = 0, len(s)

        for i in range(k):
            s_hash += get_ascii(s[i])*pow(power, k-i-1, modulo)
            s_hash %= modulo

        ans = ""
        if s_hash % modulo == hashValue:
            ans = s[i-k+1:i+1]

        for i in range(k, n):
            s_hash -= get_ascii(s[i-k])*pow(power, k-1, modulo)
            s_hash *= power
            s_hash += get_ascii(s[i])
            s_hash %= modulo
            
            if s_hash % modulo == hashValue:
                ans = s[i-k+1:i+1]

        return ans[::-1]
            
 