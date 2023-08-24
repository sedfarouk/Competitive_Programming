# 151. Leetcode - Reverse words in a string 

class Solution:
    def reverseWords(self, s: str) -> str:
        lst = reversed(s.split())
        return " ".join(lst)
