class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        MOD = (10 ** 9) + 7
        base = 27 # instead of 26 to prevent hash values of 0
        n, m = len(haystack), len(needle)

        if n < m:
            return -1

        def getAsc(ch):
            return ord(ch) - 96

        needleHash = 0
        for i in range(m):
            needleHash = (needleHash * base + getAsc(needle[i])) % MOD

        haystackHash = 0
        constantFirst = base ** (m - 1)
        for i in range(n):
            if i >= m:
                haystackHash -= getAsc(haystack[i - m]) * constantFirst

            haystackHash = (haystackHash * base + getAsc(haystack[i])) % MOD

            if i >= m - 1 and haystackHash == needleHash:
                p, q = i - m + 1, 0
                while q < m and haystack[p] == needle[q]:
                    p += 1; q += 1

                if q == m:
                    return i - m + 1

        return -1
            
