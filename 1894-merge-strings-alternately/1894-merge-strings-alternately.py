class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lst = []
        shortestWordLength = min(len(word1), len(word2))
        for i in range(shortestWordLength):
            lst.append(word1[i])
            lst.append(word2[i])
        lst.append(word1[shortestWordLength:])
        lst.append(word2[shortestWordLength:])
        return ''.join(lst)
    
word = Solution().mergeAlternately("Farouk", "Alhassan")
print(word)
         