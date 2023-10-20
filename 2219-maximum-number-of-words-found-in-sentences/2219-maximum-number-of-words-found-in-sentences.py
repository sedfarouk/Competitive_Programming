class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0

        for sentence in sentences:
            ans = max(ans, sentence.count(' ') + 1)
        
        return ans