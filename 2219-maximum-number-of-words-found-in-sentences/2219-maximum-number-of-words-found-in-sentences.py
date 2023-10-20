class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0

        for sentence in sentences:
            line = sentence.split()
            ans = max(ans, len(line))
        
        return ans