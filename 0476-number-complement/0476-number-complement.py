class Solution:
    def findComplement(self, num: int) -> int:
        k = num.bit_length()
        return num ^ (2**k)-1