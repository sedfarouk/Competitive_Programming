class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s1, s2 = set(), set()

        for c in word:
            if c.islower():
                s1.add(c)
            else:
                s2.add(c.lower())

        return len(s1 & s2)
