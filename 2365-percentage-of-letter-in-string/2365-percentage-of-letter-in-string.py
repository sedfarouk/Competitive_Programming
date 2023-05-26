class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        num = s.count(letter)
        return floor((num/len(s))*100)