class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        cost = sum(neededTime)
        largestTime = neededTime[0]

        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                largestTime = max(largestTime, neededTime[i])
            else:
                cost -= largestTime
                largestTime = neededTime[i]

        cost -= largestTime
        return cost
        