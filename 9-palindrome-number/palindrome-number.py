class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        y = 0
        xc = x
        while xc > 0:
            r = xc % 10
            y = y * 10 + r
            xc //= 10

        return x == y
