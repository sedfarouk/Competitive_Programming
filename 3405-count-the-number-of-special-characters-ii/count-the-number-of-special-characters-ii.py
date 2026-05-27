class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s1, s2  = set(), set()
        s3 = set()

        for idx, c in enumerate(word):
            cl = c.lower()
            if c.islower():
                if cl in s2:
                    s3.add(cl)
                s1.add(cl)
            else:
                s2.add(cl)

        return len((s1 & s2) - s3)