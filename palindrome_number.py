class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        for i in range(0, len(y)):
            if y[i] != y[len(y)-1-i]:
                return False
        return True