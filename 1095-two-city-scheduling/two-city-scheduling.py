class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)
        ans = a = b = 0

        for x, y in costs:
            if (a < n and x < y) or b == n:
                ans += x
                a += 1
            else:
                ans += y
                b += 1

        return ans
