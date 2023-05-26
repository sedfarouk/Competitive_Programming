class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lst = []
        longestWordLength = max(len(word1), len(word2))
        for i in range(longestWordLength):
            if i < len(word1):
                lst.append(word1[i])
            if i < len(word2):
                lst.append(word2[i])
        return ''.join(lst)
    

         