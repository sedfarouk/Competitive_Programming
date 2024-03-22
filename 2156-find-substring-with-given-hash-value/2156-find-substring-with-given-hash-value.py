class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        s = s[::-1]
        s_hash, n = 0, len(s)
        p = pow(power, k-1, modulo)

        for i in range(k):
            s_hash += (ord(s[i])-96)*pow(power, k-i-1, modulo)
            s_hash %= modulo

        ans = ""
        if s_hash % modulo == hashValue:
            ans = s[i-k+1:i+1]

        for i in range(k, n):
            s_hash -= (ord(s[i-k])-96)*p
            s_hash *= power
            s_hash += (ord(s[i])-96) % modulo
            
            if s_hash % modulo == hashValue:
                ans = s[i-k+1:i+1]

        return ans[::-1]
            
 
