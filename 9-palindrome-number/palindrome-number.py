class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10

        return x == rev or x == rev // 10

        # CAUSES INT OVERFLOW
        # y = 0
        # xc = x
        # while xc > 0:
        #     r = xc % 10
        #     y = y * 10 + r
        #     xc //= 10

        # return x == y
