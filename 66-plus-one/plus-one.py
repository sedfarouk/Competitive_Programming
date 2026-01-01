class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digits = digits[::-1]
        carry = 1

        for i in range(n):
            x = digits[i]
            digits[i] = (x + 1) % 10

            if x != 9:
                return digits[::-1]

        digits.append(1)
        return digits[::-1]

        

