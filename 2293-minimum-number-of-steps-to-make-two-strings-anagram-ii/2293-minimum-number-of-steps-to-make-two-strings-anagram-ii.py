class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_letters, t_letters = [0]*26, [0]*26

        for i in s:
            s_letters[ord(i)-ord('a')] += 1

        for i in t:
            t_letters[ord(i)-ord('a')] += 1
        
        for i in range(len(s_letters)):
            s_letters[i] = abs(s_letters[i]-t_letters[i])
        
        return sum(s_letters)
        
