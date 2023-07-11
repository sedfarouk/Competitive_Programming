class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        if needle==haystack:
            return 0
        for i in range(len(haystack)):
            if haystack[i]==needle[0]:
                if haystack[i:i+l]==needle[:l]:
                    return i
        return -1