class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n-1):
            num = str(bin(i))

            if num != num[::-1]:
                return False
        return True
        