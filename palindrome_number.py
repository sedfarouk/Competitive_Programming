class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        if y[0] == y[-1]:
            return True
        return False