class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return n^((2**n.bit_length())-1)==n>>1