class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        ans = curr = 0

        while curr < k and happiness[-1] - curr >= 0:
            ans += happiness.pop() - curr
            curr += 1

        return ans

        