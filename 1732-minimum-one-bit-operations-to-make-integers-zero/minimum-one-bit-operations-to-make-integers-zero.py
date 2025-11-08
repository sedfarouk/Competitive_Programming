class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0

        for i in range(n.bit_length()):
            if n & (1 << i): ans = ((1 << (i + 1)) - 1) - ans

        return ans