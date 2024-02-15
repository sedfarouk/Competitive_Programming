class Solution:
    def findComplement(self, num: int) -> int:
        k = 2
        while k <= num:
            k *= 2   
        return num ^ (k-1)