class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        mnC1, mnC2 = min(cost1, costBoth), min(cost2, costBoth)
        mnN = min(need1, need2)
        ans1 = costBoth * mnN + mnC1 * (need1 - mnN) + mnC2 * (need2 - mnN)
        ans2 = mnC1 * need1 + mnC2 * need2

        return min(ans1, ans2)