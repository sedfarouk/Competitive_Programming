class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s1 = s2 = 0
        s3 = (1 << 27) - 1

        for idx, c in enumerate(word):
            x = ord(c.lower()) - 97
            if c.islower():
                if s2 & (1 << x):
                    s3 &= ~(1 << x)
                s1 |= (1 << x)
            else:
                s2 |= (1 << x)

        return bin(s1 & s2 & s3).count('1')