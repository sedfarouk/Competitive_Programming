class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        temp = [1, neededTime[0], neededTime[0]]

        for i in range(1, len(colors)):
            if colors[i]==colors[i-1]:
                temp[0] += 1
                temp[1] += neededTime[i]
                temp[2] = max(temp[2], neededTime[i])
            else:
                if temp[0] > 1:
                    ans += temp[1]
                    ans -= temp[2]
                temp = [1, neededTime[i], neededTime[i]]

        if temp[0] > 1:
            ans += temp[1]
            ans -= temp[2]
        
        return ans
        