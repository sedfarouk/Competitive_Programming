class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        length = len(cardPoints)-k
        window = sum(cardPoints[:length])
        maxx = total - window
        
        for i in range(length, len(cardPoints)):
            window -= cardPoints[i-length]
            window += cardPoints[i]
            maxx = max(maxx, total-window)
            
        return maxx



        