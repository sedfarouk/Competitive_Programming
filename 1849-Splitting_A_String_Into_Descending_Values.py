class Solution:
    def splitString(self, s: str, lastVal=None) -> bool:
        if lastVal and int(s)==lastVal-1:
            return True

        for i in range(1, len(s)):
            curr = int(s[:i])

            if lastVal is None or curr==lastVal-1:
                if self.splitString(s[i:], curr):
                    return True
        return False
