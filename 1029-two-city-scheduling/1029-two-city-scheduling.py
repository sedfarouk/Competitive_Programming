class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = [(abs(a-b), a, b) for a, b in costs]
        diffs.sort(reverse=True)
        ans = a = b = 0

        for i in range(len(diffs)):
            if (diffs[i][1] < diffs[i][2] and a < len(costs)//2) or b==len(costs)//2:
                ans += diffs[i][1]
                a += 1
            else:
                ans += diffs[i][2]
                b += 1

        return ans



        

        