class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []

        for num in spells:
            req = bisect_left(potions, ceil(success/num))
            ans.append(len(potions) - req)

        return ans
        