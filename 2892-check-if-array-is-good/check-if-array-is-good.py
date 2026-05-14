class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1

        if n == 0: return False

        base = [1] * n
        base[-1] += 1

        for num in nums:
            if num > n or not base[num - 1]: return False
            base[num - 1] -= 1

        return all(x == 0 for x in base)

