class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)

        ans = True
        i = 0

        while i < n - 1:
            if bits[i]:
                i += 2
            else:
                i += 1
            
        return i == n - 1
        