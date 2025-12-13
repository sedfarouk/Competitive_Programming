class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Knuth-Morris-Pratt (KMP) Algorithm
        # TC: Guaranteed O(n + m)
        # SC: O(m)
         
        n, m = len(haystack),len(needle)
        needleLps = [0] * m

        i, j = 0, 1
        while j < m:
            if needle[i] == needle[j]:
                needleLps[j] = i + 1
                i += 1; j += 1
            elif i == 0:
                j += 1
            else:
                i = needleLps[i - 1]

        i = j = 0
        while j < n:
            if haystack[j] == needle[i]:
                i += 1; j += 1
            elif i == 0:
                j += 1
            else:
                i = needleLps[i - 1]

            if i == m:
                return j - m
        
        return -1

        