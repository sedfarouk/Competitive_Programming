class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        maxx = max(0, satisfaction[0])
                
        for i in range(1, len(satisfaction)):
            summ = satisfaction[i] + sum(satisfaction[:i])
            if maxx + summ < maxx:
                return maxx
            maxx += summ 
        return maxx
                
        