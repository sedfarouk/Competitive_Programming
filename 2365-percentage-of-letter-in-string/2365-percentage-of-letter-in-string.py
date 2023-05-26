class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        num = 0        
        for i in s:
            if i==letter:
                num+=1
        return floor((num/len(s))*100)
        