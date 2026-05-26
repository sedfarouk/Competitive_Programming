class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s0, s1, s2 = set(), set(), set()

        for c in word:
            if c.islower():
                s1.add(c)
            else:
                s2.add(c)
            if c.lower() in s1 and c.upper() in s2:
                s0.add(c.lower())

        return len(s0)
