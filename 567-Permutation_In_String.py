# 567 Leetcode - Permutation In String

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        alphabets = [0]*26
        s1_letters = [0]*26
        l = len(s1)

        for i in s1:
            s1_letters[ord(i)-ord('a')]+=1  

        for i in range(l):
            alphabets[ord(s2[i])-ord('a')]+=1

        left, right = 0, l

        while right < len(s2):
            if alphabets == s1_letters:
                return True
            alphabets[ord(s2[left])-ord('a')]-=1
            alphabets[ord(s2[right])-ord('a')]+=1
            right+=1
            left+=1
        
        if alphabets == s1_letters: return True

        return False
        
