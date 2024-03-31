class Solution:
    def repeatedStringMatch(self, a: str, pattern: str) -> int:
        n, m = len(pattern), len(a)
        lps = [0]*n
        prevLps, i = 0, 1

        while i < n:
            if pattern[i]==pattern[prevLps]:
                lps[i] = prevLps+1
                i += 1
                prevLps += 1
            elif prevLps==0:
                i += 1            
            else:
                prevLps = lps[prevLps-1]

        a *= math.ceil((n+m-1)/m)

        patternIdx = 0
        for idx, ch in enumerate(a):
            while patternIdx and pattern[patternIdx] != ch:
                patternIdx = lps[patternIdx-1]

            if pattern[patternIdx]==ch:                
                if patternIdx==n-1:
                    return math.ceil((idx+1)/m)
                
                else:
                    patternIdx += 1

        return -1