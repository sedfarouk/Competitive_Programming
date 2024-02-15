class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        sett = [0]*n
        
        for idx, word in enumerate(words):
            for ch in word:
                sett[idx] |= 1 << (ord(ch)-97)
                
        maxx = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if (sett[i] & sett[j])==0:
                    maxx = max(maxx, len(words[i])*len(words[j]))
        return maxx
                
