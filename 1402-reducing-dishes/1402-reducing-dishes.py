class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        negs, pos = min(0, satisfaction[0]), max(0, satisfaction[0])
        maxx = max(0, satisfaction[0])
                
        for i in range(1, len(satisfaction)):
            summ = satisfaction[i] + pos + negs
            if maxx + summ < maxx:
                return maxx
            pos += max(0, satisfaction[i])
            negs += min(0, satisfaction[i])
            maxx += summ 
        return maxx
                
        
